from django.shortcuts import render
from django.http import HttpResponse

from goods.models import Categories
from main.models import BestSelling, FeaturedProducts, NewArrivals


def index(request):
    best_sellings = BestSelling.objects.all()
    featured_products = FeaturedProducts.objects.all()
    new_arrivals = NewArrivals.objects.all()

    context = {
        'best_sellings': best_sellings,
        'new_arrivals': new_arrivals,
        'featured_products': featured_products,
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
