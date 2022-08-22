from django.contrib import admin

from django.contrib.auth.models import User
from .models import Movie, Director

admin.site.register(Director)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'year', 'rating', 'budget', 'rating_status', 'director']
    list_editable = ['year', 'rating', 'budget','director']
    ordering = ['name']
    list_per_page = 10
    search_fields = ['name']
    list_filter = ['name', 'year']

    @admin.display(ordering='rating', description='рейтинг статус')
    def rating_status(self, mov_ex: Movie):
        if mov_ex.rating >= 90:
            return 'nice'
        else:
            return 'not bad'
