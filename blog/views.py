from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import BlogPostForm
from .models import Category, Post

def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Assign the logged-in user as the author
            # Assign a default category if none is provided
            if not blog_post.category:
                blog_post.category, _ = Category.objects.get_or_create(name='meta', slug='meta')
            blog_post.save()
            return redirect('blog_list')  # Replace with your desired redirect
    else:
        form = BlogPostForm()

    return render(request, 'blog/create_blog_post.html', {'form': form})

def blog_list(request):
    published_posts = Post.objects.filter(is_published=True).order_by('-created_at')  # Published posts
    unpublished_posts = Post.objects.filter(is_published=False).order_by('-created_at')  # Unpublished posts
    return render(request, 'blog/blog_list.html', {
        'published_posts': published_posts,
        'unpublished_posts': unpublished_posts,
    })
