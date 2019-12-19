# Django imports
from django.urls import path, include

# Project imports
from . import views


# URLS
urlpatterns = [
    path('', views.index, name='home'),
    path('cash-flows', views.cash_flows, name='cash_flows'),
    path('cash-flows/<ticker>', views.detail_view, name='detail_view'),
    path('list-view', views.list_view, name='list_view'),
]
