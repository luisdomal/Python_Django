"""Movies app schema"""

from django.shortcuts import get_object_or_404

import graphene
from graphene.types.scalars import ID
from graphene_django import DjangoObjectType

from movies.models import Movie, Director


class MovieType(DjangoObjectType):
    """Movie object type"""

    class Meta:
        model = Movie
        fields = "__all__"


class DirectorType(DjangoObjectType):
    """Director object type"""

    class Meta:
        model = Director
        fields = "__all__"


class Query:
    """Query object type"""
    all_movies = graphene.List(MovieType)
    get_movie = graphene.Field(MovieType, pk=graphene.ID(required=True))
    all_directors = graphene.List(DirectorType)
    get_director = graphene.Field(DirectorType, pk=graphene.ID(required=True))

    def resolve_all_movies(root, info):
        return Movie.objects.select_related('director').all()

    def resolve_get_movie(root, info, pk):
        return get_object_or_404(Movie, pk=pk)

    def resolve_all_directors(root, info):
        return Director.objects.all()

    def resolve_get_director(root, info, pk):
        return get_object_or_404(Director, pk=pk)


# Mutations

class CreateDirectorMutation(graphene.Mutation):
    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        birthday = graphene.Date(required=True)

    director = graphene.Field(DirectorType)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, birthday):
        director = Director.objects.create(first_name=first_name, last_name=last_name, birthday=birthday)
        # Notice we return an instance of this mutation
        return CreateDirectorMutation(director=director)

class DeleteMovieMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
    
    message = graphene.String()

    @classmethod
    def mutate(cls, root, info, id):
        movie = get_object_or_404(Movie, id=id)
        movie.delete()
        return DeleteMovieMutation(message="Se elimino la película")

class UpdateMovieMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String(required=True)
        release_date = graphene.Date(required=True)
        rating = graphene.Int(required=True)
    
    movie = graphene.Field(MovieType)

    @classmethod
    def mutate(cls, root, info, id, name, release_date, rating):
        movie = get_object_or_404(Movie, id=id)
        movie.name = name
        movie.release_date = release_date
        movie.rating = rating
        movie.save()

        return UpdateMovieMutation(movie=movie)

class CreateMovieMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        release_date = graphene.Date(required=True)
        rating = graphene.Int(required=True)
        director_id = graphene.Int(required=True)

    movie = graphene.Field(MovieType)

    @classmethod
    def mutate(cls, root, info, name, release_date, rating, director_id):
        movie = Movie.objects.create(name=name, release_date=release_date, rating=rating, director_id=director_id)
        return CreateMovieMutation(movie=movie)

class Mutation:
    create_movie = CreateMovieMutation.Field()
    create_director = CreateDirectorMutation.Field()
    delete_movie = DeleteMovieMutation.Field()
    update_movie = UpdateMovieMutation.Field()