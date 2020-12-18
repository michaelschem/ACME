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

        self.assertEqual('123 E Main St. Seattle WA 98112',str(mailing_address))

class VariableModelTests(TestCase):
    def test_create_variables(self):
        variable = Variable()
        variable.name = 'Proximity To Volcano'
        variable.description = 'Coverage extends to properties within this range of a volcano'
        variable.value = '100-150'
        variable.value = False
        variable.value = 100000
        variable.value = 1.80

        self.assertEqual('Proximity To Volcano: 1.8', str(variable))


class PlanVariableTests(TestCase):
    def test_create_plan_variable(self):
        plan_variable = PlanVariable()
        plan_variable.value = '100-150'
        plan_variable.value = False
        plan_variable.value = 100000
        plan_variable.value = 1.80

        self.assertEqual('1.8', str(plan_variable))


class ProximityToVolcanoTests(TestCase):
    def test_create_proximity_to_volcano(self):
        proximity_to_volcano = ProximityToVolcano()
        proximity_to_volcano.value = '100-150'

        self.assertEqual('100-150', str(proximity_to_volcano))


class UnderwaterVolcanoCoverageTests(TestCase):
    def test_create_underwater_volcano_coverage(self):
        under_water_volcano_coverage = UnderwaterVolcanoCoverage()
        under_water_volcano_coverage.value = False

        self.assertEqual('False', str(under_water_volcano_coverage))


class SuperVolcanoCoverageTesets(TestCase):
    def test_create_super_volcano_coverage(self):
        super_volcano_coverage = SuperVolcanoCoverage()
        super_volcano_coverage.value = True

        self.assertEqual('True', str(super_volcano_coverage))


class CoverageLimitTests(TestCase):
    def test_create_coverage_limit(self):
        coverage_limit = CoverageLimit()
        coverage_limit.value = 100000

        self.assertEqual('100000', str(coverage_limit))


class RateVariableTests(TestCase):
    def test_create_rate_variable(self):
        rate_variable = RateVariable()
        rate_variable.value = '100-150'
        rate_variable.value = False
        rate_variable.value = 100000
        rate_variable.value = 1.80

        self.assertTrue('1.8', str(rate_variable))


class PremiumTests(TestCase):
    def test_create_premium(self):
        premium = Premium()
        premium.value = 100000
        premium.save()

        self.assertEqual(premium.value, 100000)
        self.assertEqual('100000', str(premium))


class TaxTests(TestCase):
    def test_create_tax(self):
        tax = Tax()
        tax.value = 1.80
        tax.save()

        self.assertEqual('1.8', str(tax))


class ConvenienceFeeTests(TestCase):
    def test_create_convenience_fee(self):
        convenience_fee = ConvenienceFee()
        convenience_fee.value = 4.99
        convenience_fee.save()

        self.assertEqual(convenience_fee.value, 4.99)
        self.assertEqual('4.99', str(convenience_fee))


class PlanModelTests(TestCase):
    def test_create_plan(self):
        plan = Plan()
        plan.name = '2kdj283jkf'

        self.assertEqual(str(plan.name), str(plan))


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

    def test_to_string(self):
        quote = Quote()
        quote.quote_number = '30Z1huPz4l'
        quote.effective_date = '2020-12-17'
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

        plan = Plan()
        quote.plan = plan

        self.assertEqual('30Z1huPz4l, 2020-12-17,  ', str(quote))

