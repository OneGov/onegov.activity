import re

from collections import defaultdict, namedtuple
from datetime import date
from decimal import Decimal
from itertools import groupby
from lxml import etree
from onegov.activity.models import InvoiceItem
from pprint import pformat


DOCUMENT_NS_EX = re.compile(r'.*<Document [^>]+>(.*)')
INVALID_CODE_CHARS_EX = re.compile(r'[^Q0-9A-F]+')
CODE_EX = re.compile(r'Q{1}[A-F0-9]{10}')


def normalize_xml(xml):
    # let's not bother with namespaces at all
    return DOCUMENT_NS_EX.sub(r'<Document>\1', xml)


class Transaction(object):

    __slots__ = (
        'amount',
        'booking_date',
        'booking_text',
        'credit',
        'currency',
        'debitor',
        'debitor_account',
        'note',
        'reference',
        'valuta_date',
        'username',
        'confidence',
    )

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

        self.username = None
        self.confidence = 0

    def __repr__(self):
        return pformat({key: getattr(self, key) for key in self.__slots__})


def extract_transactions(xml):
    root = etree.fromstring(normalize_xml(xml).encode('utf-8'))

    def first(element, xpath):
        elements = element.xpath(xpath)
        return elements[0] if elements else None

    def joined(element, xpath):
        return '\n'.join(element.xpath(xpath))

    def as_decimal(text):
        if text:
            return Decimal(text)

    def as_date(text):
        if text:
            return date(*[int(p) for p in text.split('-')])

    for entry in root.xpath('/Document/BkToCstmrStmt/Stmt/Ntry'):
        booking_date = as_date(first(entry, 'BookgDt/Dt/text()'))
        valuta_date = as_date(first(entry, 'ValDt/Dt/text()'))
        booking_text = first(entry, 'AddtlNtryInf/text()')

        for d in entry.xpath('NtryDtls/TxDtls'):
            yield Transaction(
                booking_date=booking_date,
                valuta_date=valuta_date,
                booking_text=booking_text,
                amount=as_decimal(first(d, 'Amt/text()')),
                currency=first(d, 'Amt/@Ccy'),
                reference=first(d, 'RmtInf/Strd/CdtrRefInf/Ref/text()'),
                note=joined(d, 'RmtInf/Ustrd/text()'),
                credit=first(d, 'CdtDbtInd/text()') == 'CRDT',
                debitor=first(d, 'RltdPties/Dbtr/Nm/text()'),
                debitor_account=first(d, 'RltdPties/DbtrAcct/Id/IBAN/text()')
            )


def extract_code(text):
    """ Takes a bunch of text and tries to extract a code from it.

    :return: The code without formatting and in lowercase or None

    """

    text = text.replace('\n', '').strip()

    if not text:
        return None

    # ENTER A WORLD WITHOUT LOWERCASE
    text = text.upper()

    # replace all O-s (as in OMG) with 0.
    text = text.replace('O', '0')

    # normalize the text by removing all invalid characters.
    text = INVALID_CODE_CHARS_EX.sub('', text)

    # try to fetch the code
    match = CODE_EX.search(text)

    if match:
        return match.string.lower()
    else:
        return None


def match_camt_053_to_usernames(xml, collection, invoice):
    """ Takes an ISO20022 camt.053 file and matches it with the invoice
    items in the :class:`~onegov.activity.collections.InvoiceItemCollection`.

    Raises an error if the given xml cannot be processed.

    :return: A list of transactions found in the xml file, together with
    the matching username and a confidence attribute indicating how
    certain the match is (1.0 indicating a sure match, 0.5 a possible match
    and 0.0 a non-match).

    """

    # Get the items matching the given invoice
    q = collection.query()
    q = q.with_entities(
        InvoiceItem.username,
        InvoiceItem.code,
        InvoiceItem.amount
    )
    q = q.filter(
        InvoiceItem.paid == False,
        InvoiceItem.invoice == invoice
    )
    q = q.order_by(
        InvoiceItem.username
    )

    # Sum up the items to virtual invoices
    invoices = []
    Invoice = namedtuple('Invoice', ('username', 'code', 'amount'))

    for username, items in groupby(q, key=lambda i: i.username):
        amount = Decimal('0.00')

        for item in items:
            amount += item.amount

        invoices.append(Invoice(
            username=username,
            code=item.code,
            amount=amount
        ))

    # Hash the invoices by code (duplicates are technically possible)
    by_code = defaultdict(list)

    # Hash the invoices by the rounded amount, to be tolerant of amounts
    # which are slightly off.
    by_amount = defaultdict(list)

    for invoice in invoices:
        by_code[invoice.code].append(invoice)
        by_amount[round(invoice.amount)].append(invoice)

    # go through the transactions, comparing amount and code for a match
    for transaction in extract_transactions(xml):
        code = extract_code(transaction.note)
        amnt = round(transaction.amount)

        code_usernames = {i.username for i in by_code.get(code, tuple())}
        amnt_usernames = {i.username for i in by_amount.get(amnt, tuple())}

        if code_usernames and amnt_usernames:
            combined = code_usernames & amnt_usernames

            if len(combined) == 1:
                transaction.username = next(u for u in combined)
                transaction.confidence == 1
            else:
                transaction.username = next(u for u in combined)
                transaction.confidence == 0.5
        elif code_usernames:
            transaction.username = next(u for u in code_usernames)
            transaction.confidence == 0.5
        elif amnt_usernames:
            transaction.username = next(u for u in amnt_usernames)
            transaction.confidence == 0.5

        yield transaction