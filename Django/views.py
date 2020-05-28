from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    title= "Index"
    context = {"title": title}
    if request.user.is_authenticated:
        context = {"title": title, "my_list": ["Monday", "Tuesday", "Wednesday"]}
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About us"})

def contact_page(request):
    return render(request, "contact.html", {"title": "Contact us"})