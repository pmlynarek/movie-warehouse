from django.contrib import admin
from moviewarehouse.movies.models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")


admin.site.register(Movie, MovieAdmin)
