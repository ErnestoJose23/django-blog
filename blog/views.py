from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.

from .models import BlogPost

#Get = 1 object
#Filter = [] objects
def blog_post_detail_page(request, slug):
    queryset = BlogPost.objects.filter(slug=slug)
    if queryset.count() == 0:  
        raise Http404
    obj = queryset.first()
    template_name = 'blog_post_detail.html'
    context = {"object": obj}

    return render(request, template_name, context)