from django.urls import path

from .views import (
    ForumListView,
    ForumDetailView,
    ForumUpdateView,
    ForumDeleteView,
    ForumCreateView
)

urlpatterns = [
    path('', ForumListView.as_view(), name='forum_list'),
    path('<slug:slug>', ForumDetailView.as_view(), name='forum_detail'),
    path('<uuid:pk>/edit/', ForumUpdateView.as_view(), name='forum_edit'),
    path('<uuid:pk>/delete/', ForumDeleteView.as_view(), name='forum_delete'),
    path('new/', ForumCreateView.as_view(), name='forum_new'),
]