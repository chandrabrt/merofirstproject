from __future__ import unicode_literals
from django.core.urlresolvers import reverse
from django.db import models


# Create your models here.


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.album_title + ' + ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null= True)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250, null=False)
    audio_file = models.FileField(null=False)
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:create_song', kwargs={'pk': self.pk})

    def __str__(self):
        return self.song_title + "." + self.file_type
