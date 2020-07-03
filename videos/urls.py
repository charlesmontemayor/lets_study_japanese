from django.urls import path

from .views import VideoListView, VideoDetailView

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
    path('<slug:slug>', VideoDetailView.as_view(), name='video_detail'),
]