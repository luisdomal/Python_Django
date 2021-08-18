"""Heroes app views"""

from django.shortcuts import get_object_or_404

from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Hero
from .serializers import HeroSerializer, HeroModelSerializer


# Viewsets

class HeroesViewSet(ModelViewSet):
    """Heroes viewset"""
    queryset = Hero.objects.all()
    serializer_class = HeroModelSerializer


# CBV genéricas

class HeroesListView(generics.ListCreateAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroModelSerializer


class HeroesDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroModelSerializer


# CBV genéricas-genéricas donde hay que especificar mixins y métodos

class GenericHeroesListView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class GenericHeroesDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    queryset = Hero.objects.all()
    serializer_class = HeroSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Estas son CBV normales

class FirstHeroesListView(APIView):
    """Heroes list views"""

    def get(self, request):
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class FirstHeroesDetailView(APIView):
    """Heroes detail views"""

    def get(self, request, pk):
        hero = get_object_or_404(Hero, pk=pk)
        serializer = HeroSerializer(hero)
        return Response(serializer.data)

    def put(self, request, pk):
        hero = get_object_or_404(Hero, pk=pk)
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        hero = get_object_or_404(Hero, pk=pk)
        hero.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


# Decorators - FBV

@api_view(['GET', 'POST'])
def heroes_list(request):
    """Show all heroes"""
    if request.method == 'GET':
        heroes = Hero.objects.all()
        serializer = HeroSerializer(heroes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = HeroSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def heroes_detail(request, pk):
    """Get a hero"""
    hero = get_object_or_404(Hero, pk=pk)
    if request.method == 'GET':
        serializer = HeroSerializer(hero)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = HeroSerializer(hero, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    if request.method == 'DELETE':
        hero.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)