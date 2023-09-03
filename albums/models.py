from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    caption = models.CharField(max_length=200)