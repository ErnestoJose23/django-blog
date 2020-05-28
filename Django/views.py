from django.http import HttpResponse

def home_page(request):
    return HttpResponse("<h1>Hola que tal</h1>")

def about_page(request):
    return HttpResponse("<h1>About us</h1>")

def contact_page(request):
    return HttpResponse("<h1>Contact us</h1>")