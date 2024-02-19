from django.contrib import admin
from main.models import BestSelling, FeaturedProducts, NewArrivals

@admin.register(BestSelling)
class BestSellingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

@admin.register(FeaturedProducts)
class featuredProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(NewArrivals)
class NewArrivalsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

