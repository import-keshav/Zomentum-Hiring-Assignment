from django.contrib import admin

from .models import (
	Ticket,
)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
	list_display = ('show', 'user','id')
	search_fields = ('show', 'user','id')
