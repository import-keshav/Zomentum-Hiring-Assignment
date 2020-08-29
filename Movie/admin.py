from django.contrib import admin

from .models import (
	Movie,
	MovieShow
)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
	list_display = ['name', 'description', 'language', 'id']
	search_fields = ['name', 'language', 'description', 'id']
	list_filter = ['language']


@admin.register(MovieShow)
class MovieShowAdmin(admin.ModelAdmin):
	list_display = ['movie', 'start_time', 'screen_number', 'id']
	search_fields = ['movie', 'start_time', 'screen_number', 'id']
	list_filter = ['movie', 'screen_number']
