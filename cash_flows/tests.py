# Django imports
from django.test import TestCase

# Project imports
from .models import StatementsOfCashFlows
from .cash_flows import get_report


# Basic Tests
class BasicTest(TestCase):
    def test_database_model(self):
        cash_flows = StatementsOfCashFlows()
        cash_flows.ticker = 'PLNT'
        cash_flows.table = '<tbody><tr><td></td></tr></tbody>'
        cash_flows.save()

        obj = StatementsOfCashFlows.objects.get(ticker='PLNT')
        self.assertEqual(obj, cash_flows)

    def test_selenium(self):
        report = get_report('ZEN')
        self.assertEqual(report[:7], '<tbody>')
