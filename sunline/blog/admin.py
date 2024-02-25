from django.contrib import admin
from . import models
from mptt.admin import MPTTModelAdmin


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "create_at", "id"]


admin.site.register(models.Category, MPTTModelAdmin)
admin.site.register(models.Tag)
admin.site.register(models.Comment)