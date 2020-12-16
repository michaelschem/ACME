from django.test import TestCase, Client


class PlanViewTests(TestCase):
    fixtures = ['api.yaml']

    def test_get_plan(self):
        c = Client()
        plans = c.get('/api/plan/').content.decode('utf-8')
        print()
