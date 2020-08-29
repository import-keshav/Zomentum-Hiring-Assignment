from django.urls import path

from . import views

urlpatterns = [
	path('create-movie', views.CreateMovie.as_view()),
	path('get-movies', views.ListMovies.as_view()),
	path('create-movie-show', views.CreateMovieShow.as_view()),
	path('get-movie-show/<int:movie_id>', views.ListMovieMovieShow.as_view()),
	path('update-movie-show/<int:pk>', views.UpdateMovieMovieShow.as_view()),
	path('get-movies-shows', views.ListMoviesShows.as_view()),
]