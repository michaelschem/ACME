from django.test import TestCase, Client

from rest_framework.test import APIRequestFactory

from api.serializers import QuoteSerializer, PlanSerializer
from api.models import Plan


class QuoteSerializerTests(TestCase):
    fixtures = ['api.yaml']

    def test_serialze_quote(self):
        request_factory = APIRequestFactory()
        request = request_factory.post('/api/quote/')
        validated_data = {
            "mailing_address": {"line1": "123 E Main St.", "city": "Seattle", "state": "WA", "zip_code": 98112},
            "quote_number": "30Z1huPz4l", "effective_date": "2020-12-17", "previous_policy_cancelled": False,
            "property_mileage_to_nearest_volcano": 100.0, "owns_property_to_be_insured": True,
            "property_address": {"line1": "321 E Main St.", "city": "Seattle", "state": "WA", "zip_code": 98112},
            "plan_id": "6c296d4cef9a42d1ace5fb037485e82f"}
        serializer = QuoteSerializer(data=validated_data, context={"request": request})
        serializer.create(validated_data)


class PlanSerializerTests(TestCase):
    fixtures = ['api.yaml']

    def test_serialize_plan(self):
        validated_data = {
            'name': 'Example Plan', 'plan_variables': [
                {'name': 'Proximity To Volcano', 'description': 'Coverage extends to properties within this range of a volcano', 'value': '100-150'},
                {'name': 'Underwater Volcano Coverage', 'description': 'Coverage includes volcanoes located underwater', 'value': False},
                {'name': 'Supervolcano Coverage', 'description': 'Coverage includes Supervolcanoes', 'value': True},
                {'name': 'Coverage Limit', 'description': 'Plan coverage limit', 'value': 100000.0}],
            'rate_variables': [
                {'name': 'Premium', 'description': 'Plan premium', 'value': 100000},
                {'name': 'Tax', 'description': 'Total tax', 'value': 1.8},
                {'name': 'Convenience Fee', 'description': 'Policy processing convenience fee', 'value': 4.99}]}
        PlanSerializer(validated_data)

    def test_deserialize_plan(self):
        expected_serialization = {'id': '10e55ffd-49c8-4181-b90c-502ad2b3f1b0', 'name': 'Great Plan', 'plan_variables': [{'name': 'Proximity To Volcano', 'description': 'Coverage extends to properties within this range of a volcano', 'value': '150-200'}, {'name': 'Underwater Volcano Coverage', 'description': 'Coverage includes volcanoes located underwater', 'value': True}, {'name': 'Supervolcano Coverage', 'description': 'Coverage includes Supervolcanoes', 'value': True}, {'name': 'Coverage Limit', 'description': 'Plan coverage limit', 'value': 200000.0}], 'rate_variables': [{'name': 'Premium', 'description': 'Plan premium', 'value': 10000}, {'name': 'Tax', 'description': 'Total tax', 'value': 2.2}, {'name': 'Convenience Fee', 'description': 'Policy processing convenience fee', 'value': 4.99}]}
        serialization = PlanSerializer(Plan.objects.first()).data
        self.assertEqual(expected_serialization, serialization)

