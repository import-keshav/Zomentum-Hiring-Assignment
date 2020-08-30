from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255,)
    mobile = models.CharField(max_length=10)

    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    def __str__(self):
        return self.name
