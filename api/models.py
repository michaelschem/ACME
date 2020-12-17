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


class Variable(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.TextField()
    description = models.TextField()
    value = None


class PlanVariable(Variable):
    value = None


class ProximityToVolcano(PlanVariable):
    value = models.TextField()


class UnderwaterVolcanoCoverage(PlanVariable):
    value = models.BooleanField()


class SuperVolcanoCoverage(PlanVariable):
    value = models.BooleanField()


class CoverageLimit(PlanVariable):
    value = models.FloatField()


class RateVariable(Variable):
    value = None


class Premium(RateVariable):
    value = models.IntegerField()


class Tax(RateVariable):
    value = models.FloatField()


class ConvenienceFee(RateVariable):
    value = models.FloatField()


class Plan(models.Model):
    """
    ACME Insurance’s Volcano Insurance product provides multiple coverage options to individuals that live within a
    certain proximity of a volcano. ACME has a strict convention around how their plans are structured, which you will
    need to take into account when creating your API. A plan consists of a ​name,​ a list of ​plan_variables,​ and a list
    of rate_variables​.

    """

    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.TextField()

    # plan_variables
    proximity_to_volcano = models.ForeignKey(ProximityToVolcano, on_delete=models.CASCADE)
    underwater_volcano_coverage = models.ForeignKey(UnderwaterVolcanoCoverage, on_delete=models.CASCADE)
    super_volcano_coverage = models.ForeignKey(SuperVolcanoCoverage, on_delete=models.CASCADE)
    coverage_limit = models.ForeignKey(CoverageLimit, on_delete=models.CASCADE)

    # rate_variables
    premium = models.ForeignKey(Premium, on_delete=models.CASCADE)
    tax = models.ForeignKey(Tax, on_delete=models.CASCADE)
    convenience_fee = models.ForeignKey(ConvenienceFee, on_delete=models.CASCADE)

    # TODO: make this more helpful, get it in table format in admin.
    def __str__(self):
        return f"{self.id}"





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
    plan = models.ForeignKey(Plan, related_name='quotes', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
