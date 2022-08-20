from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg
from .models import Movie


def show_all_movie(request):
    movies = Movie.objects.order_by('name')
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    # movies = Movie.objects.order_by(F('name').desc(nulls_last=True))
    # for i in movies:
    #     i.save()
    return render(request, 'movie_app/all_movies.html', context=
    {
        'movies': movies,
        'agg': agg,
        'total': movies.count()
    })


def show_one_movie(request, slug_movie: str):
    # movie = Movie.objects.get(id=id_movie)
    movie = get_object_or_404(Movie, id=slug_movie)
    return render(request, 'movie_app/one_movie.html', context={'movie': movie})
