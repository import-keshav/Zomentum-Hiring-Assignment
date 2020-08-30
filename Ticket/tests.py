import json
from rest_framework import status
from rest_framework.test import APITestCase

from Ticket import models as ticket_models

movie = {
    "name": "Race",
    "description": "Bollywood Thriller/Action Movie",
    "language": "Hindi",
    "cast": "Saif Ali Khan, Akshaye Khanna, Katrina Kaif",
    "duration_min": "125",
    "director": "Abbas Burmawalla"
}

movie_show = {
    "movie": "1",
    "start_time": "13:00",
    "screen_number":"1"
}

user = {
    "name": "Keshav",
    "mobile": "9643906878",
    "show_id": "1"
}


class TicketAppTests(APITestCase):
    """ Test Class for testing Ticket app API's"""
    def test_book_ticket(self):
        """     Test Book Ticket API    """
        response = self.client.post('/movie/create-movie',
            movie, format='json')
        response = self.client.post('/movie/create-movie-show',
            movie_show, format='json')
        response = self.client.post('/ticket/book-ticket',
            user, format='json')

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'message': 'Ticket Booked Succesfully',
            'ticket_id': 1
        })
        self.assertEqual(
            (ticket_models.Ticket.objects.filter(
                show__pk=1, user__mobile="9643906878")
                .count()),1)


    def test_delete_ticket(self):
        """     Test Book Ticket API    """
        response = self.client.post('/movie/create-movie',
            movie, format='json')
        response = self.client.post('/movie/create-movie-show',
            movie_show, format='json')
        response = self.client.post('/ticket/book-ticket',
            user, format='json')
        response = self.client.delete('/ticket/delete-ticket/1')
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(
            (ticket_models.Ticket.objects.filter(
                show__pk=1, user__mobile="9643906878")
                .count()),0)


    def test_get_user_details_on_ticket_id(self):
        """     Test Get User Details On Ticket API    """
        response = self.client.post('/movie/create-movie',
            movie, format='json')
        response = self.client.post('/movie/create-movie-show',
            movie_show, format='json')
        response = self.client.post('/ticket/book-ticket',
            user, format='json')
        response = self.client.get(
            '/ticket/get-ticket/1', format='json')

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content), [{
                "id":1,
                "user": {
                    "id":1,
                    "name":"Keshav",
                    "mobile":"9643906878",
                },
                "show":1
            }]
        )
