from django.urls import path
from wishlist import views

app_name = 'wishlist'


urlpatterns = [
    #path('wishlist/', views.wishlist, name="wishlist"),
    path('wishlist_add/', views.wishlist_add, name="wishlist_add"),
    path("remove-from-wishlist/", views.remove_wishlist, name="remove-from-wishlist")
]