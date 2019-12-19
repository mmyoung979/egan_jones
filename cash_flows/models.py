# Django imports
from django.db import models

# Python imports
from datetime import datetime

# Consolidated Statements of Cash Flow for individual company
class StatementsOfCashFlows(models.Model):
    ticker = models.CharField(max_length=5)
    table = models.TextField()
    date_pulled = models.DateTimeField(blank=True, default=datetime.now())
