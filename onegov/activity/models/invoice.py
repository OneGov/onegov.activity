from onegov.activity import utils
from onegov.activity.models.invoice_item import InvoiceItem, SCALE
from onegov.core.orm import Base
from onegov.core.orm.mixins import TimestampMixin
from onegov.core.orm.types import UUID
from onegov.user import User
from sqlalchemy import and_
from sqlalchemy import select
from sqlalchemy import func
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Text
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import object_session, relationship
from uuid import uuid4


class Invoice(Base, TimestampMixin):
    """ A grouping of invoice items. """

    __tablename__ = 'invoices'

    #: the public id of the invoice
    id = Column(UUID, primary_key=True, default=uuid4)

    #: the period to which this invoice belongs to
    period_id = Column(UUID, ForeignKey('periods.id'), nullable=False)

    #: the user to which the invoice belongs
    user_id = Column(UUID, ForeignKey('users.id'), nullable=False)
    user = relationship(User, backref="invoices")

    #: the code of the invoice used to identify the invoice through e-banking
    code = Column(Text, nullable=False)

    #: the specific items linked with this invoice
    items = relationship(InvoiceItem, backref='invoice')

    @property
    def display_code(self):
        """ The invoice code, formatted in a human readable format. """
        return utils.format_invoice_code(self.code)

    @property
    def esr_code(self):
        """ The invoice code, formatted as ESR. """
        return utils.encode_invoice_code(self.code)

    @property
    def display_esr_code(self):
        """ The invoice ESR formatted in a human readable format. """
        return utils.format_esr_reference(self.esr_code)

    def sync(self):
        items = object_session(self).query(InvoiceItem).filter(and_(
            InvoiceItem.source != None,
            InvoiceItem.source != 'xml'
        )).join(InvoiceItem.payments)

        for item in (i for i in items if i.payments):
            for payment in item.payments:

                # though it should be fairly rare, it's possible for
                # charges not to be captured yet
                if payment.state == 'open':
                    payment.charge.capture()
                    payment.sync()

            # the last payment is the relevant one
            item.paid = item.payments[-1].state == 'paid'

    def add(self, group, text, unit, quantity, **kwargs):
        item = InvoiceItem(
            group=group,
            text=text,
            unit=unit,
            quantity=quantity,
            invoice_id=self.id,

            # deprecated
            code=self.code,
            **kwargs
        )

        self.items.append(item)
        object_session(self).flush()

        return item

    # paid or not
    @hybrid_property
    def paid(self):
        return self.outstanding_amount <= 0

    # paid + unpaid
    @hybrid_property
    def total_amount(self):
        return self.outstanding_amount + self.paid_amount

    @total_amount.expression
    def total_amount(cls):
        return select([func.sum(InvoiceItem.amount)]).\
            where(InvoiceItem.invoice_id == cls.id).\
            label('total_amount')

    # paid only
    @hybrid_property
    def outstanding_amount(self):
        return round(
            sum(item.amount for item in self.items if not item.paid),
            SCALE
        )

    @outstanding_amount.expression
    def outstanding_amount(cls):
        return select([func.sum(InvoiceItem.amount)]).\
            where(and_(
                InvoiceItem.invoice_id == cls.id,
                InvoiceItem.paid == False
            )).label('outstanding_amount')

    # unpaid only
    @hybrid_property
    def paid_amount(self):
        return round(
            sum(item.amount for item in self.items if item.paid),
            SCALE
        )

    @paid_amount.expression
    def paid_amount(cls):
        return select([func.sum(InvoiceItem.amount)]).\
            where(and_(
                InvoiceItem.invoice_id == cls.id,
                InvoiceItem.paid == True
            )).label('paid_amount')
