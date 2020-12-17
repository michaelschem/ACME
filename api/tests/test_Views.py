import json

from django.test import TestCase, Client
from api.models import Quote, Address


class QuoteViewTests(TestCase):
    fixtures = ['api.yaml']

    def test_get_quote(self):
        right_quote = '[{"id":"0d97fc46-6c44-45d4-a2f0-df4df7d1c111","quote_number":"30Z1huPz4l","effective_date":"2020-12-17","previous_policy_cancelled":false,"property_mileage_to_nearest_volcano":100.0,"owns_property_to_be_insured":true,"mailing_address":{"line1":"123 E Main St.","city":"Seattle","state":"WA","zip_code":98112},"property_address":{"line1":"321 E Main St.","city":"Seattle","state":"WA","zip_code":98112},"plan_id":"4f788924-d61f-4d11-ac60-17f62f9e47b7"}]'
        c = Client()
        quote = c.get('/api/quote/', {'id': '0d97fc46-6c44-45d4-a2f0-df4df7d1c111'}).content.decode('utf-8')
        self.assertEqual(right_quote, quote)

    def test_get_all_quotes(self):
        righ_quotes = '[{"id":"0d97fc46-6c44-45d4-a2f0-df4df7d1c111","quote_number":"30Z1huPz4l","effective_date":"2020-12-17","previous_policy_cancelled":false,"property_mileage_to_nearest_volcano":100.0,"owns_property_to_be_insured":true,"mailing_address":{"line1":"123 E Main St.","city":"Seattle","state":"WA","zip_code":98112},"property_address":{"line1":"321 E Main St.","city":"Seattle","state":"WA","zip_code":98112},"plan_id":"4f788924-d61f-4d11-ac60-17f62f9e47b7"},{"id":"a8b5908e-3a1b-4ec8-b71a-2a8b296a5df4","quote_number":"w9dk28fh2P","effective_date":"2020-12-17","previous_policy_cancelled":true,"property_mileage_to_nearest_volcano":90.02,"owns_property_to_be_insured":false,"mailing_address":{"line1":"13555 Fiji Way","city":"Marina Del Rey","state":"CA","zip_code":90292},"property_address":{"line1":"408 W Manchester","city":"Playa Del Rey","state":"CA","zip_code":90292},"plan_id":"4f788924-d61f-4d11-ac60-17f62f9e47b7"}]'
        c = Client()
        quote = c.get('/api/quote/').content.decode('utf-8')
        self.assertEqual(righ_quotes, quote)

    def test_get_non_existent_quote(self):
        right_quote = '[]'
        c = Client()
        quote = c.get('/api/quote/', {'id': 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'}).content.decode('utf-8')
        self.assertEqual(right_quote, quote)

    def test_get_bad_uuid(self):
        c = Client()
        quote = c.get('/api/quote/', {'id': 'bad id'}).content.decode('utf-8')
        raise NotImplementedError('Not Implemented')

    def test_create_quote(self):
        raise NotImplementedError('Not Implemented')


class PlanViewTests(TestCase):
    fixtures = ['api.yaml']

    def test_get_plan(self):
        c = Client()
        plans = c.get('/api/plan/').content.decode('utf-8')
        raise NotImplementedError('Not Implemented')

    def test_get_all_plans(self):
        c = Client()
        raise NotImplementedError('Not Implemented')


