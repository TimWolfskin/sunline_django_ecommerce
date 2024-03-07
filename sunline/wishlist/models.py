from django.db import models
from goods.models import Products
from users.models import User



class WishlistQueryset(models.QuerySet):
    
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0

    

class Wishlist(models.Model):

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='user')
    product = models.ForeignKey(to=Products, on_delete=models.CASCADE, verbose_name='Product')
    quantity = models.PositiveSmallIntegerField(default=0, verbose_name='Quantity')
    session_key = models.CharField(max_length=32, null=True, blank=True)
    created_timestamp = models.DateTimeField(auto_now_add=True, verbose_name='Date added')

    class Meta:
        db_table = 'Wishlist'
        verbose_name = "Wishlist"
        verbose_name_plural = "Wishlist"

    objects = WishlistQueryset().as_manager()




    def __str__(self):
        if self.user:
            return f'Wishlist {self.user.username} | Product {self.product.name} | Quantity {self.quantity}'
            
        return f'Anonymous wishlist | Product {self.product.name} | Quantity {self.quantity}'