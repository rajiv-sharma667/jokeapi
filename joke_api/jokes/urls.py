from django.urls import path
from .views import fetch_and_store_jokes

urlpatterns = [
    path('fetch-jokes/', fetch_and_store_jokes, name='fetch-jokes'),
]