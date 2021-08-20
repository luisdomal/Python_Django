"""Movies app models"""

from django.db import models


class Movie(models.Model):
    """Movie model"""
    name = models.CharField(max_length=255)
    release_date = models.DateField()
    rating = models.PositiveSmallIntegerField()
    director = models.ForeignKey("Director", on_delete=models.CASCADE)

    def __str__(self):
        """Return movie name"""
        return self.name


class Director(models.Model):
    """Director model"""
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()

    def __str__(self):
        """Return director's full name"""
        # f"{1 + 1} de {self.birthday}"
        # "{} de {}".format(1 + 1, self.birthday)
        return f"{self.first_name} {self.last_name}"