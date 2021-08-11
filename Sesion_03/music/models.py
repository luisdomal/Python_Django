""" Music app models """

from django.db import models

class Artist(models.Model):
    """Artist Model"""
    # id = models.AutoField(primary_key=True) "Este campo no es necesario ponerlo en automativo Django lo crea."
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Album(models.Model):
    """ Album Model"""
    title = models.CharField(max_length=255)
    # Creamos la llave foranea de la sigueinte forma.
    # on_delete es un protocolo que usamos CASCADE para eliminar todos Albums de ese artista.
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Song(models.Model):
    """ Song Model """
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.FileField(upload_to='music/')

    def __str__(self):
        return self.title

