from django.urls import path, 
from .views import (
    blog_post_create_view,
    blog_post_list_view,
    blog_post_detail_view,
    blog_post_update_view,
    blog_post_delete_view,
)


urlpatterns = [
    path('blog/<str:slug>/', blog_post_detail_view),
    path('blog/<str:slug>/edit/', blog_post_update_view),
    path('blog/<str:slug>/delete/', blog_post_delete_view),
    path('blog/', blog_post_list_view),
    path('blog-new/', blog_post_create_view),
]
