from django.shortcuts import render, redirect

from .models import Director, Movie, Year


def list_movies(request):
    """List all songs"""
    movies = Movie.objects.all().order_by('director__name', 'title')
    context = {"movies": movies}
    return render(request, 'movies/list_movie.html', context)


def add_movie(request):
    """Add a new movie"""
    if request.method == "POST":
        director_name = request.POST.get("director_name")
        movie_title = request.POST.get("movie_title")
        film_year = request.POST.get("film_year")
        director, _created = Director.objects.get_or_create(name=director_name)
        film_year, _created = Year.objects.get_or_create(year=film_year)
        movie = Movie(title=movie_title, director=director, year=film_year)
        movie.save()
        return redirect("movies:list")

    return render(request, 'movies/add_movie.html')