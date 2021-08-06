from django.shortcuts import render, redirect

from .models import Song, Artist, Album


def list_songs(request):
    """List all songs"""
    songs = Song.objects.all().order_by('artist__name', 'title')
    context = {"songs": songs}
    return render(request, 'music/song_list.html', context)


def create_song(request):
    """Create a new song"""
    if request.method == "POST":
        song_title = request.POST.get("song_title")
        artist_name = request.POST.get("artist_name")
        album_title = request.POST.get("album_title")
        artist, _created = Artist.objects.get_or_create(name=artist_name)
        album, _created = Album.objects.get_or_create(title=album_title, artist=artist)
        song = Song(title=song_title, artist=artist, album=album)
        song.save()
        return redirect("music:list")

    return render(request, 'music/song_create.html')