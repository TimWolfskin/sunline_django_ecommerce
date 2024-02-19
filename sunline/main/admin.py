from django.contrib import admin
from main.models import BestSelling, FeaturedProducts

@admin.register(BestSelling)
class BestSellingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(FeaturedProducts)
class featuredProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

