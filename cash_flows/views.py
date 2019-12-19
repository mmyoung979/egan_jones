# Django imports
from django.shortcuts import render

# Python imports
from datetime import datetime

# Project imports
from .forms import CashFlowsForm
from .models import StatementsOfCashFlows
from .cash_flows import get_report


# Homepage
def index(request):
    form = CashFlowsForm()
    context = {'form': form,}
    return render(request, 'index.html', context)

# Consolidated Statements of Cash Flows by search
def cash_flows(request):
    form = CashFlowsForm(request.POST or None)
    context = {'form': form}

    if form.is_valid():
        ticker = form.cleaned_data.get('ticker')
        context['ticker'] = ticker.upper()

        # If ticker is already in database, load info
        if StatementsOfCashFlows.objects.filter(ticker=context['ticker']).count():
            obj = StatementsOfCashFlows.objects.filter(ticker=context['ticker'])[0]
            context['report'] = obj.table
            context['time'] = obj.date_pulled

        # If ticker is not already in database, get info and save
        else:
            try:
                context['report'] = get_report(ticker)
                context['time'] = datetime.now()

            # If ticker does not exist, return error page
            except:
                return render(request, 'error.html', context)

            statement = StatementsOfCashFlows.objects.create(
                ticker=context['ticker'],
                table=context['report'],
                date_pulled=datetime.now(),
            )

    return render(request, 'cash_flows.html', context)

# List View
def list_view(request):
    form = CashFlowsForm()
    context = {
        'form': form,
        'list': StatementsOfCashFlows.objects.order_by('ticker'),
    }
    return render(request, 'list-view.html', context)

# Detail View
def detail_view(request, ticker):
    obj = StatementsOfCashFlows.objects.filter(ticker=ticker)[0]
    context = {
        'form': CashFlowsForm(initial={'ticker': ticker}),
        'ticker': ticker,
        'report': obj.table,
        'time': obj.date_pulled,
    }
    return render(request, 'cash_flows.html', context)
