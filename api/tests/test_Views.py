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
            "plan_id": "4f788924-d61f-4d11-ac60-17f62f9e47b7"}
        serializer = QuoteSerializer(data=validated_data, context={"request": request})
        # serializer.create(validated_data)
        serializer.is_valid()
        # serializer.save()


class PlanViewTests(TestCase):
    fixtures = ['api.yaml']

    def test_get_plan(self):
        c = Client()
        plans = c.get('/api/plan/').content.decode('utf-8')

    # def test_get_all_plans(self):
    #     c = Client()
    #     raise NotImplementedError('Not Implemented')


