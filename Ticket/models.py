from django.db import models

from Movie import models as movie_models
from User import models as user_models


class Ticket(models.Model):
    """ Ticket Model """
    show = models.ForeignKey(movie_models.MovieShow,
        on_delete=models.CASCADE, related_name="movie_show_ticket")
    user = models.ForeignKey(user_models.User,
        on_delete=models.CASCADE, related_name="user_ticket")
    is_expired = models.BooleanField(default=False)
    class Meta:
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'
