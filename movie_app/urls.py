from . import views
from django.urls import path

urlpatterns = [
    path('', views.show_all_movie),
    path('movie/<slug:slug_movie>', views.show_one_movie, name='movie-detail'),
    path('directors/', views.all_directors, name='all_directors'),
    path('directors/<int:id_dir>', views.one_director, name='one_director')
]
