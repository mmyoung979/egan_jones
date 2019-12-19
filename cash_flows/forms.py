# Django imports
from django import forms

# Search / Add Form
class CashFlowsForm(forms.Form):
    ticker = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control mr-sm-2',
        'placeholder': 'Search tickers (i.e. aapl)',
    }))
