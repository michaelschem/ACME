from django.test import TestCase, Client


class QuoteViewTests(TestCase):
    fixtures = ['api.yaml']

    def test_get_quote(self):
        c = Client()
        quote = c.get('/api/quote/', {id: 1}).content.decode('utf-8')
