# Django imports
from django.shortcuts import render

# Project imports
from .cash_flows import get_report

def index(request):
    context = {}
    return render(request, 'index.html', context)

def cash_flows(request, ticker):
    context = {
        'ticker': ticker.upper(),
        'report': get_report(ticker),
    }
    return render(request, 'cash_flows.html', context)
