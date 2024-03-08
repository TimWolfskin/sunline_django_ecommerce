from django.shortcuts import render


from main.models import BestSelling, FeaturedProducts, NewArrivals
from blog.models import Post


def index(request):
    best_sellings = BestSelling.objects.all()
    featured_products = FeaturedProducts.objects.all()
    new_arrivals = NewArrivals.objects.all()
    posts = Post.objects.all()

    context = {
        'new_arrivals': new_arrivals,
        'featured_products': featured_products,
        "title": "Sunline - main page",
        "content": "furniture ecommerce Sunline",
        'best_sellings': best_sellings,
        "posts": posts
    }
    return render(request, "main/index.html", context)


def best_selling(request, best_selling_slug):
    best_selling = BestSelling.objects.get(slug=best_selling_slug)

    context = {
        'best_selling': best_selling
    }
    return render(request, 'main/best_product.html', context=context)
