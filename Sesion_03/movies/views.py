from django.shortcuts import render, redirect

from .models import Director, Movie


def list_movies(request):
    """List all songs"""
    movies = Movie.objects.all().order_by('director__name', 'title')
    context = {"movies": movies}
    return render(request, 'movies/list_movies.html', context)


def add_movie(request):
    """Add a new movie"""
    if request.method == "POST":
        director_name = request.POST.get("director_name")
        movie_title = request.POST.get("movie_title")
        director, _created = Director.objects.get_or_create(name=director_name)
        movie = Movie(title=movie_title, director=director)
        movie.save()
        return redirect("movies:list")

    return render(request, 'movies/add_movie.html')