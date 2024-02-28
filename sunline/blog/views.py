from urllib import request
from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from blog.models import Post, Tag
from django.views.generic import ListView, DetailView


def blog(request):
    post_list = Post.objects.all()

    tags = Tag.objects.all()

    context = {
        "post_list": post_list,
        "tags": tags
    }
    return render(request, "blog/blog.html", context)


# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = "post"
#     slug_url_kwarg = 'post_slug'


def post_detail(request, post_slug):
    post_detail = Post.objects.get(slug=post_slug)


   

    context = {
        "post_detail": post_detail,  

    }
    return render(request, 'blog/post_detail.html', context=context)

