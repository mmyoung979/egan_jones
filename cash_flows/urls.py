# Django imports
from django.urls import path, include

# Project imports
from . import views

# URLS
urlpatterns = [
    path('', views.index, name='home'),
    path('<ticker>', views.cash_flows, name='cash_flows'),
]
