from django.urls import path

from .views import VideoListView

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
]