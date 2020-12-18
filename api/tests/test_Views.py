import json

from django.test import TestCase, Client

from rest_framework.test import APIRequestFactory

from api.serializers import QuoteSerializer
from api.views import PlanViewSet, QuoteViewSet


class QuoteViewTests(TestCase):
    fixtures = ['api.yaml']

    def test_get_quote(self):
        right_quote = '[{"id":"6b09cca4-505b-406c-93db-736fa0ecfe2b","quote_number":"30Z1huPz4l","effective_date":"2020-12-17","previous_policy_cancelled":false,"property_mileage_to_nearest_volcano":100.0,"owns_property_to_be_insured":true,"mailing_address":{"line1":"123 E Main St.","city":"Seattle","state":"WA","zip_code":98112},"property_address":{"line1":"321 E Main St.","city":"Seattle","state":"WA","zip_code":98112},"plan":"6c296d4c-ef9a-42d1-ace5-fb037485e82f"}]'
        c = Client()
        quote = c.get('/api/quote/', {'id': '6b09cca4-505b-406c-93db-736fa0ecfe2b'}).content.decode('utf-8')
        self.assertEqual(right_quote, quote)

    def test_get_all_quotes(self):
        # Shouldn't get anything because this was not a requirement and explicitly disabled
        right_quotes = '[]'
        c = Client()
        quote = c.get('/api/quote/').content.decode('utf-8')
        self.assertEqual(right_quotes, quote)

    # def test_get_non_existent_quote(self):
    #     right_quote = '[]'
    #     c = Client()
    #     quote = c.get('/api/quote/', {'id': 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'}).content.decode('utf-8')
    #     self.assertEqual(right_quote, quote)

    # def test_get_bad_uuid(self):
    #     c = Client()
    #     quote = c.get('/api/quote/', {'id': 'bad id'}).content.decode('utf-8')
    #     raise NotImplementedError('Not Implemented')
    #
    def test_create_quote(self):
        request_factory = APIRequestFactory()
        request = request_factory.post('/api/quote/')
        validated_data = {
            "mailing_address": {"line1": "123 E Main St.", "city": "Seattle", "state": "WA", "zip_code": 98112},
            "quote_number": "30Z1huPz4l", "effective_date": "2020-12-17", "previous_policy_cancelled": False,
            "property_mileage_to_nearest_volcano": 100.0, "owns_property_to_be_insured": True,
            "property_address": {"line1": "321 E Main St.", "city": "Seattle", "state": "WA", "zip_code": 98112},
            "plan_id": "6c296d4c-ef9a-42d1-ace5-fb037485e82f"}
        serializer = QuoteSerializer(data=validated_data, context={"request": request})
        # serializer.create(validated_data)
        serializer.is_valid()
        # serializer.save()


class PlanViewTests(TestCase):
    fixtures = ['api.yaml']

    def test_get_all_plans(self):
        right_plans = '[{"id":"10e55ffd-49c8-4181-b90c-502ad2b3f1b0","name":"Great Plan","plan_variables":[{"name":"Proximity To Volcano","description":"Coverage extends to properties within this range of a volcano","value":"150-200"},{"name":"Underwater Volcano Coverage","description":"Coverage includes volcanoes located underwater","value":true},{"name":"Supervolcano Coverage","description":"Coverage includes Supervolcanoes","value":true},{"name":"Coverage Limit","description":"Plan coverage limit","value":200000.0}],"rate_variables":[{"name":"Premium","description":"Plan premium","value":10000},{"name":"Tax","description":"Total tax","value":2.2},{"name":"Convenience Fee","description":"Policy processing convenience fee","value":4.99}]},{"id":"6c296d4c-ef9a-42d1-ace5-fb037485e82f","name":"Example Plan​","plan_variables":[{"name":"Proximity To Volcano","description":"Coverage extends to properties within this range of a volcano","value":"100-150"},{"name":"Underwater Volcano Coverage","description":"Coverage includes volcanoes located underwater","value":false},{"name":"Supervolcano Coverage","description":"Coverage includes Supervolcanoes","value":false},{"name":"Coverage Limit","description":"Plan coverage limit","value":100000.0}],"rate_variables":[{"name":"Premium","description":"Plan premium","value":100000},{"name":"Tax","description":"Total tax","value":1.8},{"name":"Convenience Fee","description":"Policy processing convenience fee","value":4.99}]},{"id":"94d751c4-865f-4670-8f01-db1d5139414f","name":"Excellent Plan","plan_variables":[{"name":"Proximity To Volcano","description":"Coverage extends to properties within this range of a volcano","value":"200-250"},{"name":"Underwater Volcano Coverage","description":"Coverage includes volcanoes located underwater","value":false},{"name":"Supervolcano Coverage","description":"Coverage includes Supervolcanoes","value":true},{"name":"Coverage Limit","description":"Plan coverage limit","value":200000.0}],"rate_variables":[{"name":"Premium","description":"Plan premium","value":100000},{"name":"Tax","description":"Total tax","value":1.8},{"name":"Convenience Fee","description":"Policy processing convenience fee","value":10.0}]}]'
        c = Client()
        plans = c.get('/api/plan/').content.decode('utf-8')
        self.assertEqual(3, len(json.loads(plans)))
        self.assertEqual(right_plans, plans)

    def test_get_plan(self):
        right_plan = '[{"id":"10e55ffd-49c8-4181-b90c-502ad2b3f1b0","name":"Great Plan","plan_variables":[{"name":"Proximity To Volcano","description":"Coverage extends to properties within this range of a volcano","value":"150-200"},{"name":"Underwater Volcano Coverage","description":"Coverage includes volcanoes located underwater","value":true},{"name":"Supervolcano Coverage","description":"Coverage includes Supervolcanoes","value":true},{"name":"Coverage Limit","description":"Plan coverage limit","value":200000.0}],"rate_variables":[{"name":"Premium","description":"Plan premium","value":10000},{"name":"Tax","description":"Total tax","value":2.2},{"name":"Convenience Fee","description":"Policy processing convenience fee","value":4.99}]}]'
        c = Client()
        plan = c.get('/api/plan/', {'id': '10e55ffd-49c8-4181-b90c-502ad2b3f1b0'}).content.decode('utf-8')
        self.assertEqual(1, len(json.loads(plan)))
        self.assertEqual(right_plan, plan)



