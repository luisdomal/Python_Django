"""Music app models"""

from django.db import models


class Artist(models.Model):
    """Artist model"""
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Album(models.Model):
    """Album model"""
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Song(models.Model):
    """Song model"""
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title
