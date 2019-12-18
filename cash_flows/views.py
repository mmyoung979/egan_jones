# Django imports
from django.shortcuts import render

# Project imports
from .cash_flows import get_report

def index(request, ticker):
    context = {
        'report': get_report(ticker)
    }
    return render(request, 'base.html', context)
