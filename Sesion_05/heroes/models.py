"""Hero APP Model"""

from django.db import models


class Hero(models.Model):
    """Hero model"""
    name = models.CharField(max_length=255)
    MARVEL = "mv"
    DC_COMICS = "dc"
    PUBLISHER_CHOICES = (
        (MARVEL, "Marvel"),
        (DC_COMICS, "DC Comics"),
    )
    publisher = models.CharField(max_length=2, choices=PUBLISHER_CHOICES)
    alter_ego = models.CharField(max_length=255)
    first_appearance = models.CharField(max_length=255)

    def __str__(self):
        """Return hero as a string"""
        return self.name