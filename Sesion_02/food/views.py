"""Food App Views"""

import random
from django.shortcuts import render, redirect


name = ["Mauricio", "Luis", "Jorge", "Ximena", "Luis"]
food = ["Pizza", "Sushi", "Alitas", "Hamburguesa", "Costillas a la BBQ"]
lenguajes = ["C ++", "Javascript", "Python", "Ruby", "Scala", "Java"]

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
        "lenguajes" : lenguajes
    }
    return render(request, "lenguajes.html", context)

def create_food(request):
    """Create a food"""
    if request.method == 'POST':
        name = request.POST['name']
        food.append(name)
        return redirect('food:list')

    return render(request, "create.html")