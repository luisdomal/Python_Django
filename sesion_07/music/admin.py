from django.contrib import admin

from .models import Album, Song, Artist


admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Artist)
