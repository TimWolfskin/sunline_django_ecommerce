from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post


def blog(request):
    post_list = Post.objects.all()

    context = {
        "post_list": post_list
    }
    return render(request, "blog/blog.html", context)

