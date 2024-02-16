from django.contrib import admin
from main.models import BestSelling

@admin.register(BestSelling)
class BestSellingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}