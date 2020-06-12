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
    path('<uuid:pk>/delete/', GuideDeleteView.as_view(), name='guide_delete'),
    path('<uuid:pk>/edit/', GuideUpdateView.as_view(), name='guide_edit'),
    path('<slug:slug>', GuideDetailView.as_view(), name='guide_detail'),
    path('', GuideListView.as_view(), name='guide_list')
]
