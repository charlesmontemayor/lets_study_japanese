from django.urls import path

from .views import (
    VideoListView,
    VideoDetailView,
    VideoCreateView,
    VideoDeleteView,
    )

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
    path('<uuid:pk>/delete/', VideoDeleteView.as_view(), name='video_delete'),
    path('new/', VideoCreateView.as_view(), name='video_new'),
    path('<slug:slug>', VideoDetailView.as_view(), name='video_detail'),
    
]