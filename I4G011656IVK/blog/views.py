from dataclasses import field
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import ListView
from django.views.generic.edit import DetailView
from django.views.generic.edit import UpdateView
from .models import Post
# Create your views here.
# In blog/views.py,  create a new view/class PostListView, which inherits django’s generic ListView,  it’s config/attributes should be:

# model = Post
class PostListView(ListView):
    model = Post
    field = [
        "__all__"
    ]

    success_url  = reverse_lazy('blog:all')


class PostDetailView(DetailView):
    model = Post
    field = [
        "__all__"
    ]

    
class PostDeleteView(UpdateView):
    model = Post
    field = [
        "__all__"
    ]

    success_url  = reverse_lazy('blog:all')