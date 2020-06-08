from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Guide


class GuideListView(ListView):
    model = Guide
    template_name = 'guides/guide_list.html'


class GuideDetailView(DetailView):
    model = Guide
    template_name = 'guides/guide_detail.html'


class GuideUpdateView(UpdateView):
    model = Guide
    fields = ('title', 'body')
    template_name = 'guides/guide_edit.html'


class GuideDeleteView(DeleteView):
    model = Guide
    template_name = 'guides/guide_delete.html'
    success_url = reverse_lazy('guide_list')
