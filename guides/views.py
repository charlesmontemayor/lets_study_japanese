from django.views.generic import ListView

from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'guides/post_list.html'
