from onegov.activity.models import Period
from onegov.core.collection import GenericCollection


class PeriodCollection(GenericCollection):

    @property
    def model_class(self):
        return Period

    def add(self, title, prebooking, execution, active=False):

        return super().add(
            title=title,
            prebooking_start=prebooking[0],
            prebooking_end=prebooking[1],
            execution_start=execution[0],
            execution_end=execution[1],
            active=active
        )

    def active(self):
        return self.query().filter(Period.active == True).first()