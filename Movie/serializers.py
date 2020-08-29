from rest_framework import serializers

from . import models as movie_models


class ListCreateUpdateDeleteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_models.Movie
        fields = '__all__'


class CreateUpdateDeleteMovieShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie_models.MovieShow
        fields = '__all__'


class ListMovieShowSerializer(serializers.ModelSerializer):
    movie = ListCreateUpdateDeleteMovieSerializer()
    class Meta:
        model = movie_models.MovieShow
        fields = '__all__'