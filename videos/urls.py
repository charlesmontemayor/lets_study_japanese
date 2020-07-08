from django.urls import path

from .views import (
    VideoListView,
    VideoDetailView,
    VideoCreateView,
    VideoDeleteView,
    VideoUpdateView,
    )

urlpatterns = [
    path('<uuid:pk>/edit/', VideoUpdateView.as_view(), name='video_edit'),
    path('<uuid:pk>/delete/', VideoDeleteView.as_view(), name='video_delete'),
    path('new/', VideoCreateView.as_view(), name='video_new'),
    path('<slug:slug>', VideoDetailView.as_view(), name='video_detail'),
    path('', VideoListView.as_view(), name='video_list'),
]