import uuid

from django.db import models


class Address(models.Model):
    """
    An address object that will hold all the neccessary data for a standard address.  This will primarily be used in
    the quote object.

    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    line1 = models.TextField()
    city = models.TextField()
    state = models.TextField()
    zip_code = models.IntegerField()


class Plan(models.Model):
    """
    ACME Insurance’s Volcano Insurance product provides multiple coverage options to individuals that live within a
    certain proximity of a volcano. ACME has a strict convention around how their plans are structured, which you will
    need to take into account when creating your API. A plan consists of a ​name,​ a list of ​plan_variables,​ and a list
    of rate_variables​.

    """

    # plan_variables
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.TextField()

    # TODO: make this more helpful, get it in table format in admin.
    def __str__(self):
        return f"{self.id}"


class Variable(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.TextField()
    description = models.TextField()
    value = None


class PlanVariable(Variable):
    plan = models.ManyToManyField(Plan, related_name='plan_variables')


class IntPlanVariable(PlanVariable):
    value = models.IntegerField()


class StrPlanVariable(PlanVariable):
    value = models.TextField()


class FltPlanVariable(PlanVariable):
    value = models.FloatField()


class BoolPlanVariable(PlanVariable):
    value = models.BooleanField()


class RateVariable(Variable):
    plan = models.ManyToManyField(Plan, related_name='rate_variables')


class IntRateVariable(RateVariable):
    value = models.IntegerField()


class StrRateVariable(RateVariable):
    value = models.TextField()


class FltRateVariable(RateVariable):
    value = models.FloatField()


class BoolRateVariable(RateVariable):
    value = models.BooleanField()


class Quote(models.Model):
    """
    For any insurance product we offer through Sure, a customer must answer questions in order to determine their
    eligibility and select their plan/coverage. Based on these answers, a customer is provided with a price quote prior
    to making a purchase. The quote​ object is where we store the customer’s responses.

    """
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    quote_number = models.CharField(max_length=10)
    effective_date = models.DateField()
    previous_policy_cancelled = models.BooleanField(default=False)
    property_mileage_to_nearest_volcano = models.FloatField()
    owns_property_to_be_insured = models.BooleanField()
    mailing_address = models.ForeignKey(Address, related_name='mailing_address', on_delete=models.CASCADE)
    property_address = models.ForeignKey(Address, related_name='property_address', on_delete=models.CASCADE)
    # TODO: change back to required
    plan = models.ForeignKey(Plan, related_name='quotes', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
