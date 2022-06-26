from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Post


class PostListView(ListView):
    model = Post


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