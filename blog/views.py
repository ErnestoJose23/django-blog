from django.shortcuts import render

# Create your views here.

from .models import BlogPost


def blog_post_detail_page(request, id):   
    obj = BlogPost.objects.get(id=id)
    template_name = 'blog_post_detail.html'
    context = {"object": obj}

    return render(request, template_name, context)