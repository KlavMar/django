from django.shortcuts import render
from django.views.generic import ListView,DetailView
from app.blog.models import Post,Media
# Create your views here.

class PostListView(ListView):
    queryset=Post.objects.order_by('-date_create')
    context_object_name = 'posts'
    template_name='index.html'


class PostMediaView(ListView):
    model=Media
    context_object_name = 'images'
    template_name= 'image.html'



