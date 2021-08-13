"""Tweets app URL config"""

from django.urls import path

from . import views


app_name = "tweets"
urlpatterns = [
    path("", views.TweetListView.as_view(), name="list"),
    path("create", views.CreateTweetView.as_view(), name="create"),
]