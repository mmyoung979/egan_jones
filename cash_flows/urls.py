# Django imports
from django.urls import path, include

# Project imports
from . import views

# URLS
urlpatterns = [
    path('<ticker>', views.index, name='home')
]
