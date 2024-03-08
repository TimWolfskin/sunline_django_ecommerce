from main import views
from django.contrib import admin
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('best_selling/<slug:best_selling_slug>/', views.best_selling, name='best_selling'),
]
