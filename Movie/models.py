from django.db import models
from django.core.validators import MinValueValidator


class Movie(models.Model):
    """     Movie Models    """
    name = models.CharField(max_length=300)
    description = models.TextField()
    language = models.CharField(max_length=50)
    director = models.CharField(max_length=300)
    cast = models.TextField()
    duration_min = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Movie'
        verbose_name_plural = 'Movies'
    def __str__(self):
        return self.name


class MovieShow(models.Model):
    """     Movie Show Models    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
        related_name="movie_show")
    start_time = models.TimeField()
    screen_number = models.IntegerField(validators=[MinValueValidator(0)])

    class Meta:
        verbose_name = 'Movie Show'
        verbose_name_plural = 'Movie Shows'
