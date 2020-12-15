import uuid

from django.db import models

# Create your models here.


class Plan(models.Model):
    """
    ACME Insurance’s Volcano Insurance product provides multiple coverage options to individuals that live within a
    certain proximity of a volcano. ACME has a strict convention around how their plans are structured, which you will
    need to take into account when creating your API. A plan consists of a ​name,​ a list of ​plan_variables,​ and a list
    of rate_variables​.

    """

    # plan_variables
    proximity_to_volcano = models.FloatField()
    is_underwater_coverage = models.BooleanField()
    is_super_volcano_coverage = models.BooleanField()
    coverage_limit = models.FloatField()

    # rate_variables
    premium = models.FloatField()
    tax = models.FloatField()
    convienience_fee = models.FloatField()

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
    # TODO: Use mailing address model
    mailing_address = models.TextField()
    property_address = models.TextField()
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id}"
