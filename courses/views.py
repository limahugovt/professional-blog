from django.shortcuts import render
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.filter(status='published').order_by('-publish')[:4]
    }
    return render(request, 'index.html', context)
