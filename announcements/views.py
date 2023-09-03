from django.shortcuts import render, redirect
from .models import Announcement
from .forms import AnnouncementForm
from django.contrib.auth.decorators import login_required

def home(request):
    announcements = Announcement.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'announcements': announcements})

@login_required
def create_announcement(request):
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.author = request.user
            announcement.save()
            return redirect('home') 
    else:
        form = AnnouncementForm()
    return render(request, 'announcements/create.html', {'form': form})