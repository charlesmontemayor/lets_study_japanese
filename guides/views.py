from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Guide


class GuideListView(LoginRequiredMixin, ListView):
    model = Guide
    template_name = 'guides/guide_list.html'
    context_object_name = 'guide_list'
    login_url = 'account_login'


class GuideDetailView(LoginRequiredMixin, DetailView):
    model = Guide
    template_name = 'guides/guide_detail.html'
    context_object_name = 'guide'
    login_url = 'account_login'


class GuideUpdateView(LoginRequiredMixin, UpdateView):
    model = Guide
    fields = ('title', 'body')
    template_name = 'guides/guide_edit.html'
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class GuideDeleteView(LoginRequiredMixin, DeleteView):
    model = Guide
    template_name = 'guides/guide_delete.html'
    success_url = reverse_lazy('guide_list')
    login_url = 'account_login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class GuideCreateView(LoginRequiredMixin, CreateView):
    model = Guide
    template_name = 'guides/guide_new.html'
    fields = ('title', 'body',)
    login_url = 'account_login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
