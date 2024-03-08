from django.shortcuts import render, get_list_or_404
from django.http import JsonResponse, HttpResponse
from django.core.paginator import Paginator
from goods.utils import q_search
from django.db.models import Avg, Count

from goods.models import Products, ProductReview
from goods.forms import ProductReviewForm

def catalog(request, category_slug=None):

    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    on_type = request.GET.get('on_type', None)
    on_color = request.GET.get('on_color', None)
    query = request.GET.get('q', None)

    if category_slug == 'all':
        goods = Products.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = get_list_or_404(Products.objects.filter(category__slug=category_slug))

    if on_sale:
        goods = goods.filter(discount__gt=0)
    
    if order_by and order_by != "default":
        goods = goods.order_by(order_by)

    if on_type:
        goods = goods.filter(type__icontains=on_type)

    if on_color:
        goods = goods.filter(color__icontains=on_color)

    paginator = Paginator(goods, 3)
    current_page = paginator.page(int(page))

    context = {
        'title': 'Home - catalog',
        'goods': current_page,
        "slug_url": category_slug,
    }
    return render(request, 'goods/catalog.html', context)



def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    # product = Products.objects.get(pid=pid)

    # products = Products.objects.filter(category=product.category) #.exclude(pid=pid)

    #getting all reviews related to a product
    reviews = ProductReview.objects.filter(product=product).order_by("-date")

    # #getting average review
    # average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    #review form
    review_form = ProductReviewForm()

    make_review = True

    # if request.user.is_authenticated:
    #     user_review_count = ProductReveiw.objects.filter(user=request.user, product=product).count()

    #     if user_review_count > 0:
    #         make_review = False

    # product_image = product.product_images.all()

    context = {
        "product": product,  
        "review_form": review_form,
        "make_review": make_review,
        "reviews": reviews,
        # "average_rating": average_rating,
        # "product_image": product_image,
        # "products": products
    }



    return render(request, 'goods/product.html', context=context)



def ajax_add_review(request, product_slug):
    product = Products.objects.get(pk=product_slug)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review = request.POST['review'],
        # rating = request.POST['rating'],
    )
    context = {
        'user': user.username,
        'review': request.POST['review'],
        # 'rating': request.POST['rating'],
    }
    average_reviews = ProductReview.objects.filter(product=product) #.aggregate(rating=Avg("rating"))

    return JsonResponse (
        {
            'bool': True,
            'context': context,
            'average_reviews': average_reviews
        }
    )

