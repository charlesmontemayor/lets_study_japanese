from django.urls import path

from .views import PostListView, PostDetailView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', PostListView.as_view(), name='post_list')
]
