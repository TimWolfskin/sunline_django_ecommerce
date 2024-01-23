from main import views
from django.contrib import admin
from django.urls import path

from about import views

app_name = 'about'

urlpatterns = [
    path('about/', views.about, name='about'),
]