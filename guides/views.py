from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'guides/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'guides/post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ('title', 'body')
    template_name = 'guides/post_edit.html'


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'guides/post_delete.html'
    success_url = reverse_lazy('post_list')
