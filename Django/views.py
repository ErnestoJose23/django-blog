from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm

from blog.models import BlogPost

def home_page(request):
    title= "Index"
    qs = BlogPost.objects.all()[:5]
    context = {"title": "Welcome to Django Blog", "blog_list": qs}
    return render(request, "home.html", context)

def about_page(request):
    return render(request, "about.html", {"title": "About us"})

def contact_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    context = {
        "title": "Contact us", 
        "form": form
    }
    return render(request, "contact.html", context)