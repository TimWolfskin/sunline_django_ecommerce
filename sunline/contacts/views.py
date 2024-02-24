from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from contacts.models import ContactUs


def contacts(request):
    if request.method == "POST":
        contact = ContactUs()
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact.name = name
        contact.email = email
        contact.telephone = telephone
        contact.subject = subject
        contact.message = message
        contact.save()

        # return HttpResponse('<h1>Thanks for Contact Us</h1>')
        return render(request, "contacts/success.html")
    return render(request, "contacts/contacts.html")
