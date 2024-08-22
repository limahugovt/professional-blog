from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
  name = models.CharField(max_length=100, unique=True)
  description = models.TextField(blank=True)

  def __str__(self):
    return self.name

class Post(models.Model):
  STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
  )
  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250, unique_for_date='publish')
  author = models.ForeignKey(User, on_delete=models.CASCADE,)
  content = models.TextField()
  publish = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  image = models.ImageField(upload_to='posts/', blank=False)

  class Meta:
    ordering = ('-publish',)

  def __str__(self):
    return self.title

class Comment(models.Model):
  post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
  name = models.CharField(max_length=80)
  email = models.EmailField()
  body = models.TextField()
  created = models.DateTimeField(auto_now_add=True)
  approved = models.BooleanField(default=False)

  class Meta:
    ordering = ('created',)

  def __str__(self):
    return f'Comment by {self.name} on {self.post}'