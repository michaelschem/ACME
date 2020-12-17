from django.test import TestCase, Client

from api.models import Address, Variable, PlanVariable, ProximityToVolcano

class QuoteModelTests(TestCase):
    fixtures = ['api.yaml']

    def test_create_quote(self):
        quote = Quote()
        quote.quote_number = '30Z1huPz4l'
        quote.effective_date = '1993-01-20'
        quote.previous_policy_cancelled = False
        quote.property_mileage_to_nearest_volcano = 100
        quote.owns_property_to_be_insured = True

        mailing_address = Address()
        mailing_address.line1 = '123 E Main St.'
        mailing_address.city = 'Seattle'
        mailing_address.state = 'WA'
        mailing_address.zip_code = '98112'

        property_address = Address()
        property_address.line1 = '321 E Main St.'
        property_address.city = 'Seattle'
        property_address.state = 'WA'
        property_address.zip_code = '98112'

        quote.plan_id = '4f788924d61f4d11ac6017f62f9e47b7'

        self.assertTrue(True)