# sostenibilidad_blog/views.py

from django.shortcuts import render
from blog.models import Post
from pages.models import Page

def home(request):
    # Obtiene los 3 elementos más recientes; puedes ajustar la cantidad
    latest_posts = Post.objects.all().order_by('-created_at')[:3]
    latest_pages = Page.objects.all().order_by('-created_at')[:3]
    context = {
        'latest_posts': latest_posts,
        'latest_pages': latest_pages,
    }
    return render(request, 'home.html', context)