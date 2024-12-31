from django.urls import path
from .views import create_blog_post, blog_list

urlpatterns = [
    path('create/', create_blog_post, name='create_blog_post'),
    
    path('', blog_list, name='blog_list'),  # URL for blog_list
]
