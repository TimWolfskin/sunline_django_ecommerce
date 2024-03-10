from datetime import date
from itertools import product
from django.shortcuts import render



from blog.models import Post
from goods.models import Products


def index(request):
    goods = Products.objects.all()


    posts = Post.objects.all()

    context = {
        "posts": posts,
        "goods": goods,
    }
    return render(request, "main/index.html", context)

