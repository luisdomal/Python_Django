"""Users app views"""

from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render


def users_login(request):
    """Authenticates a user"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponse("Hola {}, estás autenticado.".format(user.first_name))
    return render(request, "users/login.html")