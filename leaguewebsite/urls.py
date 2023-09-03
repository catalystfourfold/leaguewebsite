"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.views.generic.base import TemplateView

from django.conf import settings
from django.conf.urls.static import static

from .views import download_file

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('announcements.urls')),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('albums/', include('albums.urls')),
    path('links/', TemplateView.as_view(template_name='links.html'), name='links'),
    path('forms/', TemplateView.as_view(template_name='forms.html'), name='forms'),
    path('download/<str:filename>/', download_file, name='download'),
    path('howtoscore/', TemplateView.as_view(template_name='howtoscore.html'), name='howtoscore'),
    path('obituary/', TemplateView.as_view(template_name='obituary.html'), name='obituary'),
    path('rosters/', include('rosters.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

