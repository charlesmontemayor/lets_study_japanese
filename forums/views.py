from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Forum, Comment


class ForumListView(LoginRequiredMixin, ListView):
    model = Forum
    template_name = 'forums/forum_list.html'
    context_object_name = 'forum_list'
    login_url = 'account_login'

class ForumDetailView(LoginRequiredMixin, DetailView):
    model = Forum
    template_name = 'forums/forum_detail.html'
    context_object_name = 'forum'
    login_url = 'account_login'

class ForumUpdateView(LoginRequiredMixin, UpdateView):
    model = Forum
    fields = ('title', 'body')
    template_name = 'forums/forum_edit.html'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ForumDeleteView(LoginRequiredMixin, DeleteView):
    model = Forum
    template_name = 'forums/forum_delete.html'
    success_url = reverse_lazy('forum_list')
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    template_name = 'forums/forum_new.html'
    fields = ('title', 'body')
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)