from django.urls import path

from . import views

urlpatterns = [
	path('book-ticket', views.BookTicket.as_view()),
	path('get-ticket/<int:ticket_id>', views.GetTicket.as_view()),
	path('delete-ticket/<int:pk>', views.DeleteTicket.as_view()),
]