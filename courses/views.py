from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts_relevant': Post.objects.filter(relevant=True).order_by('-publish')[:1],
        'posts': Post.objects.filter(status='published').order_by('-publish')[:2]
    }
    return render(request, 'index.html', context)
