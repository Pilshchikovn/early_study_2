from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg
from .models import Movie, Director


def show_all_movie(request):
    movies = Movie.objects.order_by('name')
    # movies = Movie.objects.annotate(new_field_bool=True)
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
    movie = get_object_or_404(Movie, slug=slug_movie)
    return render(request, 'movie_app/one_movie.html', context={'movie': movie})


def all_directors(request):
    directors = Director.objects.all
    return render(request, 'movie_app/all_directors.html', {'dir': directors})


def one_director(request, id_dir: int):
    direct = get_object_or_404(Director, id=id_dir)
    return render(request, 'movie_app/one_director.html.', {'director': direct})
