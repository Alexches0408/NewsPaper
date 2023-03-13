# from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-pub_date')

class PostDeatil(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'
# Create your views here.
