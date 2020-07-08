from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'video_list'

class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    context_object_name = 'video'

class VideoDeleteView(DeleteView):
    model = Video
    template_name = 'videos/video_delete.html'
    success_url = reverse_lazy('video_list')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class VideoCreateView(CreateView):
    model = Video
    template_name = 'videos/video_new.html'
    fields = ('title', 'video',)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)