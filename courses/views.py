from django.shortcuts import render, get_object_or_404
from .models import Post, Category

def home(request):
    context = {
        'posts_relevant': Post.objects.filter(relevant=True).order_by('-publish')[:1],
        'posts_recents': Post.objects.filter(status='published').order_by('-publish')[:7],
        'categories': Category.objects.all()[:3]
    }
    return render(request, 'index.html', context)

def detail_view(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post': post}
    return render(request, 'pagePost.html', context)