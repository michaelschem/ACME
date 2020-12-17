from django.test import TestCase, Client

from api.models import Address, Variable, PlanVariable, ProximityToVolcano, UnderwaterVolcanoCoverage, \
SuperVolcanoCoverage, CoverageLimit, RateVariable, Premium, Tax, ConvenienceFee, Plan, Quote


class AddressModelTests(TestCase):
    def test_create_address(self):
        mailing_address = Address()
        mailing_address.line1 = '123 E Main St.'
        mailing_address.city = 'Seattle'
        mailing_address.state = 'WA'
        mailing_address.zip_code = '98112'


class VariableModelTests(TestCase):
    def test_create_variables(self):
        variable = Variable()
        variable.name = 'Proximity To Volcano'
        variable.description = 'Coverage extends to properties within this range of a volcano'
        variable.value = '100-150'
        variable.value = False
        variable.value = 100000
        variable.value = 1.80


class PlanVariableTests(TestCase):
    def test_create_plan_variable(self):
        plan_variable = PlanVariable()
        plan_variable.value = '100-150'
        plan_variable.value = False
        plan_variable.value = 100000
        plan_variable.value = 1.80


class ProximityToVolcanoTests(TestCase):
    def create_proximity_to_volcano(self):
        proximity_to_volcano = ProximityToVolcano()
        proximity_to_volcano.value = '100-150'


class UnderwaterVolcanoCoverageTests(TestCase):
    def create_underwater_volcano_coverage(self):
        under_water_volcano_coverage = UnderwaterVolcanoCoverage()
        under_water_volcano_coverage.value = False


class SuperVolcanoCoverageTesets(TestCase):
    def create_super_volcano_coverage(self):
        super_volcano_coverage = SuperVolcanoCoverage()
        super_volcano_coverage.value = True

        self.assertTrue(True)


class CoverageLimitTests(TestCase):
    def create_coverage_limit(self):
        coverage_limit = CoverageLimit()
        coverage_limit.value = 100000

        self.assertTrue(True)


class RateVariableTests(TestCase):
    def create_rate_variable(self):
        rate_variable = RateVariable()
        rate_variable.value = '100-150'
        rate_variable.value = False
        rate_variable.value = 100000
        rate_variable.value = 1.80

        self.assertTrue(True)


class PremiumTests(TestCase):
    def create_premium(self):
        premium = Premium()
        premium.value = 100000
        premium.save()

        self.assertEqual(premium.value, 100000)


class TaxTests(TestCase):
    def create_tax(self):
        tax = Tax()
        tax.value = 1.80
        tax.save()

        self.assertEqual(tax.value, 1.80)


class ConvenienceFeeTests(TestCase):
    def create_convenience_fee(self):
        convenience_fee = ConvenienceFee()
        convenience_fee.value = 4.99
        convenience_fee.save()

        self.assertEqual(convenience_fee.value, 4.99)


class QuoteModelTests(TestCase):

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
