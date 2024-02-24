from django.contrib import admin
from contacts.models import ContactUs

class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'subject', 'message' ]

admin.site.register(ContactUs, ContactUsAdmin)