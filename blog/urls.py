from django.urls import path
from .views import create_blog_post, post_list

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_post, name='create_blog_post'),
    
    path('posts/', post_list, name='post_list'),  # URL for post_list
]
