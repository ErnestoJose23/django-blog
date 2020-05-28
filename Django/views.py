from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title= "Index"
    return render(request, "home.html", {"title": title})

def about_page(request):
    return render(request, "about.html", {"title": "About us"})

def contact_page(request):
    return render(request, "contact.html", {"title": "Contact us"})