from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories
from main.models import BestSelling


def index(request):
    best_sellings = BestSelling.objects.all()
    context = {
        'best_sellings': best_sellings,
        "title": "Sunline - main page",
        "content": "furniture ecommerce Sunline",
    }
    return render(request, "main/index.html", context)


def about(request):
    context = {
        "title": "Sunline - about",
        "content": "About",
        "text_on_page": "why this store is so awesome and needfull",
    }
    return render(request, "main/about.html", context)


def contacts(request):
    return render(request, "main/contacts.html")
