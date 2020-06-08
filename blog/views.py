from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .forms import BlogPostForm, BlogPostModelForm
from .models import BlogPost

@staff_member_required
def blog_post_create_view(request):
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template_name = 'contact.html'
    context = {'form': form}
    return render(request, template_name, context)

def blog_post_list_view(request):
    qs = BlogPost.objects.all()
    template_name = 'blog/list.html'
    context = {'object_list': qs}
    return render(request, template_name, context)

def blog_post_detail_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/detail.html'
    context = {"object": obj}
    return render(request, template_name, context)

def blog_post_update_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/update.html'
    context = {"object": obj, 'form': None}
    return render(request, template_name, context)

def blog_post_delete_view(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    template_name = 'blog/delete.html'
    context = {"object": obj}
    return render(request, template_name, context)