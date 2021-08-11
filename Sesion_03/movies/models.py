""" Movies app models """

from django.db import models

class Director(models.Model):
    """Writer Model"""
    # id = models.AutoField(primary_key=True) "Este campo no es necesario ponerlo en automativo Django lo crea."
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Year(models.Model):
    """ Year Model"""
    year = models.IntegerField()

    def ___str___(self):
        return str(self.year)

class Movie(models.Model):
    """ Movie Model """
    title = models.CharField(max_length=255)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)  

    def __str__(self):
        return self.title

