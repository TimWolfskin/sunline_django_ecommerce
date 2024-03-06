from django.contrib import admin


from wishlist.models import Wishlist

# admin.site.register(Cart)
class WishlistTabAdmin(admin.TabularInline):
    model = Wishlist
    fields = "product", "created_timestamp"
    search_fields = "product", "created_timestamp"
    readonly_fields = ("created_timestamp",)
    extra = 1


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ["user", "product", "created_timestamp",]
    list_filter = ["created_timestamp", "user", "product__name",]
