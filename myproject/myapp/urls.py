"""
This module contains the app configuration for the urls.
"""

from django.urls import path
from .views import my_view, thanks_view, display_data_view

urlpatterns = [
    path('', my_view, name='my_view'),
    path('thanks/', thanks_view, name='thanks'),
    path('display_data/', display_data_view, name='display_data'),
]
