from main import views
from django.contrib import admin
from django.urls import path

from contacts import views

app_name = 'contacts'

urlpatterns = [
    path('contacts/', views.contacts, name='contacts'),
]