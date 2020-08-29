from django import forms
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from Movie import models as movie_models
from Movie import serializers as movie_serializer


class CreateMovie(generics.CreateAPIView):
    serializer_class = movie_serializer.ListCreateUpdateDeleteMovieSerializer


class ListMovies(generics.ListAPIView):
    serializer_class = movie_serializer.ListCreateUpdateDeleteMovieSerializer
    queryset = movie_models.Movie.objects.all()


class CreateMovieShow(generics.CreateAPIView):
    serializer_class = movie_serializer.CreateUpdateDeleteMovieShowSerializer


class ListMovieMovieShow(generics.ListAPIView):
    serializer_class = movie_serializer.ListMovieShowSerializer

    def get_queryset(self):
    	return movie_models.MovieShow.objects.filter(movie__pk=self.kwargs['movie_id'])


class UpdateMovieMovieShow(generics.UpdateAPIView):
    serializer_class = movie_serializer.CreateUpdateDeleteMovieShowSerializer
    queryset = movie_models.MovieShow.objects.all()


class ListMoviesShows(generics.ListAPIView):
    serializer_class = movie_serializer.ListMovieShowSerializer
    queryset = movie_models.MovieShow.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['start_time']
