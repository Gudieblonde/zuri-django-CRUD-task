from dataclasses import field
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView
from django.views.generic.edit import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from .models import Post


class PostCreateView(CreateView):
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

class PostUpdateView(UpdateView):
    model = Post
    field = [
        "__all__"
    ]
    
class PostDeleteView(DeleteView):
    model = Post
    field = [
        "__all__"
    ]

    success_url  = reverse_lazy('blog:all')

    template_name = 'home.html'