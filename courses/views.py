from django.shortcuts import render
from .models import Post, Category

def home(request):
    context = {
        'posts_relevant': Post.objects.filter(relevant=True).order_by('-publish')[:1],
        'posts_recents': Post.objects.filter(status='published').order_by('-publish')[:2],
        'all_posts': Post.objects.filter(status='published').order_by('-publish')[:6],
        'categories': Category.objects.all()[:3]
    }
    return render(request, 'index.html', context)
