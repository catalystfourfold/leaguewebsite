from django.urls import path
from . import views

urlpatterns = [
    path('create_album/', views.create_album, name='create_album'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('album/<int:album_id>/add_photo/', views.add_photo, name='add_photo'),
    path('', views.albums, name='albums'),
]