from django.shortcuts import render
from django.http import HttpResponse


def about(request):
    context = {
        "title": "Sunline - about",
        "content": "About",
        "text_on_page": "why this store is so awesome and needfull",
    }
    return render(request, "about/about.html", context)


