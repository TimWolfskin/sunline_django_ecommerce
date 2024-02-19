from django.db import models
from goods.models import Categories


class BestSelling(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='best_selling_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'best selling'
        ordering = ("id",)
    
    def __str__(self):
        return self.name
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price


class FeaturedProducts(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    description = models.TextField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='featured_products_images', blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    group = models.CharField(max_length=150, unique=True, blank=True, null=True)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'featured products'
        ordering = ("id",)
    
    def __str__(self):
        return self.name
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price