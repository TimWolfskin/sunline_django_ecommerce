from django.shortcuts import render
from django.http import HttpResponse


def contacts(request):
    return render(request, "contacts/contacts.html")
