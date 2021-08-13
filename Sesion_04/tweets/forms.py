"""Tweets app forms"""

from django import forms

from .models import Tweet


class TweetModelForm(forms.ModelForm):
    """Tweet model form"""
    class Meta:
        model = Tweet
        fields = ['content']