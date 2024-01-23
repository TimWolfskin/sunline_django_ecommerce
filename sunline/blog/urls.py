from main import views
from django.contrib import admin
from django.urls import path

from blog import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.blog, name='blog'),
]