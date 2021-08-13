"""Tweets app models"""

from django.db import models

from django.contrib.auth import get_user_model

User = get_user_model()


class Tweet(models.Model):
    """Tweet model"""
    content = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of a tweet"""
        return self.content