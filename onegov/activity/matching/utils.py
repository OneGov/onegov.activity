from datetime import timedelta

from onegov.activity import log
from onegov.activity.utils import dates_overlap
from sortedcontainers import SortedSet


def overlaps(booking, other, minutes_between=0):
    """ Returns true if the two given bookings overlap. """

    assert booking != other

    offset = timedelta(seconds=minutes_between / 2 * 60)

    # make sure that 11:00 - 12:00 and 12:00 - 13:00 are not overlapping
    ms = timedelta(microseconds=1)

    return dates_overlap(
        tuple((b.start - offset, b.end + offset - ms) for b in booking.dates),
        tuple((o.start - offset, o.end + offset - ms) for o in other.dates),
    )


class LoopBudget(object):
    """ Helps ensure that a loop doesn't overreach its complexity budget.

    For example::

        budget = LoopBudget(max_ticks=10)

        while True:
            if budget.limit_reached():
                break
    """

    def __init__(self, max_ticks):
        self.ticks = 0
        self.max_ticks = max_ticks

    def limit_reached(self, as_exception=False):
        if self.ticks >= self.max_ticks:
            message = "Loop limit of {} has been reached".format(self.ticks)

            if as_exception:
                raise RuntimeError(message)
            else:
                log.warning(message)

            return True

        self.ticks += 1


def hashable(attribute):

    class Hashable(object):

        def __hash__(self):
            return hash(getattr(self, attribute))

        def __eq__(self, other):
            return getattr(self, attribute) == getattr(other, attribute)

    return Hashable


def booking_order(booking):
    """ Keeps the bookings predictably sorted from highest to lowest priority.

    """

    return booking.priority * -1, booking.id


def unblockable(accepted, blocked, key=booking_order):
    """ Returns a set of items in the blocked set which do not block
    with anything. The set is ordered using :func:`booking_order`.

    """

    unblockable = SortedSet(blocked, key=key)

    for accepted in accepted:
        for booking in blocked:
            if accepted.overlaps(booking):
                unblockable.remove(booking)

    return unblockable
