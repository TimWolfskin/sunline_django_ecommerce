from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.forms import UserLoginForm

from users.forms import UserLoginForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form = UserLoginForm()


    context = {
        "title": "Sunline - authorization",
        'form': form,
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        "title": "Sunline - registration",
    }
    return render(request, 'users/registration.html', context)

def profile(request):
    context = {
        "title": "Sunline - profile",
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...