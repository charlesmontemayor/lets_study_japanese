"""lets_study_japanese URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from pages.views import CustomPasswordChangeView

urlpatterns = [
    # Django Admin
    path('admin-japanesestudy-mc/', admin.site.urls),

    # User Management
    path('accounts/password/change/', CustomPasswordChangeView.as_view(), name='account_password_change'),
    path('accounts/', include('allauth.urls')),

    # Local Apps
    path('forums/', include('forums.urls')),
    path('accounts/', include('users.urls')),
    path('', include('pages.urls')),
    path('guides/', include('guides.urls')),
    path('videos/', include('videos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
