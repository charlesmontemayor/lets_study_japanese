from django.views.generic import ListView

from .models import Video


class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'video_list'