from django.urls import path

from .views import (
    GuideListView,
    GuideDetailView,
    GuideUpdateView,
    GuideDeleteView,
    GuideCreateView
    )

urlpatterns = [
    path('new/', GuideCreateView.as_view(), name='guide_new'),
    path('<int:pk>/delete/', GuideDeleteView.as_view(), name='guide_delete'),
    path('<int:pk>/edit/', GuideUpdateView.as_view(), name='guide_edit'),
    path('<int:pk>/', GuideDetailView.as_view(), name='guide_detail'),
    path('', GuideListView.as_view(), name='guide_list')
]
