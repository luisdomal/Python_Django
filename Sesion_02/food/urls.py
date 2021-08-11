"""Food app URL config"""

from django.urls import path

from .views import list_food, detail_food, create_food, lista_lenguajes, crear_lenguajes

app_name = 'food'
urlpatterns = [
    path('', list_food, name='list'),
    path('<int:id>', detail_food, name='detail'),
    path('create', create_food, name='create'),
    path('lenguajes', lista_lenguajes, name = 'lenguajes'),
    path('crearleng', crear_lenguajes, name='crear_leng'),
    
]