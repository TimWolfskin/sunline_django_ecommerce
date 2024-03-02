from django.contrib import admin

from goods.models import Categories, Products, ProductReview

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'quantity', 'price', 'discount']
    list_editable = ['discount']
    search_fields = ['name', 'description']
    list_filter = ['category', 'price', 'discount']







class ProductReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'review', 'date']

admin.site.register(ProductReview, ProductReviewAdmin)
