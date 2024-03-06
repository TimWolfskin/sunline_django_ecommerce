from django.db import models
from goods.models import Products
from users.models import User


    

class Wishlist(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='user')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Product')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Date added')

    class Meta:
        db_table = 'Wishlist'
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlist"