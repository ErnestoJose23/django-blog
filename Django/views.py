from django.http import HttpResponse
from django.shortcuts import render
from .forms import ContactForm

def home_page(request):
    title= "Index"
    context = {"title": title}
    if request.user.is_authenticated:
        context = {"title": title, "my_list": ["Monday", "Tuesday", "Wednesday"]}
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