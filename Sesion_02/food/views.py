"""Food App Views"""

import random
from django.shortcuts import render, redirect


name = ["Mauricio", "Luis", "Jorge", "Ximena", "Luis"]
food = ["Pizza", "Sushi", "Alitas", "Hamburguesa", "Costillas a la BBQ"]
lenguajes = ["C ++", "Javascript", "Python", "Ruby", "Scala", "Java"]
lenguajes_list = []

def list_food(request):
    context = {
        "name" : random.choice(name),
        "food" : food
    }

    return render(request, "list.html", context)

def detail_food(request, id):
    context = {
        "food" : food[int(id)]
    }
    return render(request, "detail.html", context)

def lista_lenguajes(request):
    context = {
        "lenguajes_list" : lenguajes
    }
    return render(request, "lenguajes.html", context)

def create_food(request):
    """Create a food"""
    if request.method == 'POST':
        name = request.POST['name']
        food.append(name)
        return redirect('food:list')
    return render(request, "create.html")

def crear_lenguajes(request):
    if request.method == 'POST':
        name = request.POST['name']
        lenguajes_list.append(name)
    ''' Siempre es importante crear el contexto para poder pasar la información que se quiere renderizar en la plantilla'''
    context = {
        "lenguajes": lenguajes_list,
        "lenguajes_list": lenguajes
    }
    return render(request, "crear_leng.html", context)
