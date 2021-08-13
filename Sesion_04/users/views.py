"""Users app views"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from .forms import UserForm
from tweets.models import Tweet



# Class based views


class LoginView(auth_views.LoginView):
    """Authenticates a user"""
    template_name = "users/login.html"
    redirect_authenticated_user = True


class ProfileView(LoginRequiredMixin, TemplateView):
    """Shows user's profile"""
    template_name = "users/profile.html"

    def get_context_data(self):
        """Puts tweets in context"""
        context = super().get_context_data()
        tweets = Tweet.objects.filter(user=self.request.user)
        context['tweets'] = tweets
        return context


class LogoutView(auth_views.LogoutView):
    """Logs out a user"""


class SignupView(FormView):
    """Register a user"""
    form_class = UserForm
    success_url = reverse_lazy("users:profile")
    template_name = "users/signup.html"

    def form_valid(self, form):
        """Saves a user"""
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


# Function based views

def users_login(request):
    """Authenticates a user"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("users:profile")
    return render(request, "users/login.html")


@login_required
def profile(request):
    """Shows user's profile"""
    return render(request, "users/profile.html")


@login_required
def users_logout(request):
    """Log out a user"""
    logout(request)
    return redirect("users:login")


def sign_up(request):
    """Creates a new user"""
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("users:profile")

    return render(request, "users/signup.html", {"form": form})