from django.shortcuts import render, redirect
from .models import Album, Photo
from .forms import AlbumForm, PhotoForm
from django.db.models import Prefetch
from django.contrib.auth.decorators import login_required

def albums(request):
    albums_with_photos = Album.objects.prefetch_related(Prefetch('photo_set', queryset=Photo.objects.all(), to_attr='photos'))
    return render(request, 'albums/albums.html', {'albums_with_photos': albums_with_photos})

@login_required
def create_album(request):
    if request.method == 'POST':
        form = AlbumForm(request.POST)
        if form.is_valid():
            album = form.save()
            return redirect('albums')
    else:
        form = AlbumForm()
    return render(request, 'albums/create_album.html', {'form': form})

def album_detail(request, album_id):
    album = Album.objects.get(id=album_id)
    photos = album.photo_set.all()
    return render(request, 'albums/album_detail.html', {'album': album, 'photos': photos})

@login_required
def add_photo(request, album_id):
    album = Album.objects.get(id=album_id)
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.album = album
            photo.save()
            return redirect('albums')
    else:
        form = PhotoForm(initial={'album': album})
    return render(request, 'albums/add_photo.html', {'form': form, 'album': album})