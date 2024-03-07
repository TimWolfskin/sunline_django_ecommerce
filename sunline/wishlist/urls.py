from django.urls import path
from wishlist import views

app_name = 'wishlist'


urlpatterns = [
    #path('wishlist/', views.wishlist, name="wishlist"),
    path('wishlist_add/', views.wishlist_add, name="wishlist_add"),
    path('wishlist_change/', views.wishlist_change, name='wishlist_change'),
    path("wishlist_remove/", views.wishlist_remove, name="wishlist_remove")
]