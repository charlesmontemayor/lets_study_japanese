from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

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
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ForumDeleteView(LoginRequiredMixin, DeleteView):
    model = Forum
    template_name = 'forums/forum_delete.html'
    success_url = reverse_lazy('forum_list')
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class ForumCreateView(LoginRequiredMixin, CreateView):
    model = Forum
    template_name = 'forums/forum_new.html'
    fields = ('title', 'body')
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ForumUserListView(LoginRequiredMixin, ListView):
    model = Forum
    template_name = 'forums/forum_by_user.html'
    context_object_name = 'forums_by_user'
    login_url = 'account_login'
    
    def get_queryset(self):
        self.request.user = get_object_or_404(get_user_model(), username=self.kwargs['username'])
        return Forum.objects.filter(user = self.request.user)
