"""My movies URL Configuration"""

from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt #Esto solo es para quitar la validación en Insomnia o Grphql por metodo POST

from graphene_django.views import GraphQLView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]