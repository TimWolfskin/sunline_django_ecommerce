from email.policy import default
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from users.models import User
from django.urls import reverse

# RATING = (
#     (1, '⭐✭✭✭✭'),
#     (2, '⭐⭐✭✭✭'),
#     (3, '⭐⭐⭐✭✭'),
#     (4, '⭐⭐⭐⭐✭'),
#     (5, '⭐⭐⭐⭐⭐'),
# )

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='category', default='category.jpg')

    class Meta:
        db_table = 'category'
    
    def __str__(self):
        return self.name


class Products(models.Model):
    # pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet='abcdefgh12345') 
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, unique=True)
    image = models.ImageField(upload_to='goods_images', blank=True, null=True)
    description = models.TextField(max_length=200, unique=True, blank=True, null=True)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2)
    color = models.CharField(max_length=50, blank=True, null=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True)

    quantity = models.PositiveIntegerField(default=0)


    class Meta:
        db_table = 'product'
        ordering = ("id",)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    
    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price*self.discount/100, 2)
        
        return self.price
    


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name="reviews")
    review = models.TextField(blank=True, null=True)
    # rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Product Reviews"

    def __str__(self):
        return self.product.name
    
    # def get_rating(self):
    #     return self.rating