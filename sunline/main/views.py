from django.shortcuts import render


from main.models import BestSelling, FeaturedProducts, NewArrivals
from blog.models import Post


def index(request):
    best_sellings = BestSelling.objects.all()
    featured_products = FeaturedProducts.objects.all()
    new_arrivals = NewArrivals.objects.all()
    posts = Post.objects.all()

    context = {
        'best_sellings': best_sellings,
        'new_arrivals': new_arrivals,
        'featured_products': featured_products,
        "title": "Sunline - main page",
        "content": "furniture ecommerce Sunline",
        "posts": posts
    }
    return render(request, "main/index.html", context)





