"""Tweets app views"""

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView, ListView
from django.urls import reverse_lazy

from .forms import TweetModelForm
from .models import Tweet


class TweetListView(ListView):
    """Shows all tweets"""
    queryset = Tweet.objects.all()
    template_name = "tweets/list.html"


class CreateTweetView(LoginRequiredMixin, FormView):
    """Creates a new tweet"""
    form_class = TweetModelForm
    template_name = "tweets/create.html"
    success_url = reverse_lazy("users:profile")

    def form_valid(self, form):
        tweet = form.save(commit=False)
        tweet.user = self.request.user
        tweet.save()
        return super().form_valid(form)