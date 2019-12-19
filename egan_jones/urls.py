# Django imports
from django.contrib import admin
from django.urls import path, include

# Project Imports
from cash_flows import urls as cash_flows_urls


# URLS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(cash_flows_urls))
]
