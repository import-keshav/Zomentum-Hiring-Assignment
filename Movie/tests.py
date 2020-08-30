import json
from rest_framework import status
from rest_framework.test import APITestCase

from Movie import models as movie_models


movie_1 = {
    "name": "Race",
    "description": "Bollywood Thriller/Action Movie",
    "language": "Hindi",
    "cast": "Saif Ali Khan, Akshaye Khanna, Katrina Kaif",
    "duration_min": "125",
    "director": "Abbas Burmawalla"
}

movie_2 = {
    "name": "The Fate of the Furious",
    "description": "Hollywood Thriller/Action Movie",
    "language": "English",
    "cast": "Vin Diesel, Dwayne Johnson, Jason Statham",
    "duration_min": "125",
    "director": "F. Gary Gray"
}

movie_show_1 = {
    "movie": "1",
    "start_time": "13:00",
    "screen_number":"1"
}

new_timimg_movie_show_1 = {
    "movie": "1",
    "start_time": "15:00",
    "screen_number":"1"
}

movie_show_2 = {
    "movie": "2",
    "start_time": "13:00",
    "screen_number":"1"
}


class MovieAppTests(APITestCase):
    """ Test Class for testing Ticket app API's"""
    def test_create_movie(self):
        """     Test Create Movie API   """
        response = self.client.post('/movie/create-movie',
            movie_1, format='json')

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            'id': 1,
            'name': 'Race',
            'description': 'Bollywood Thriller/Action Movie',
            'language': 'Hindi',
            'director': 'Abbas Burmawalla',
            'cast': 'Saif Ali Khan, Akshaye Khanna, Katrina Kaif',
            'duration_min': 125
        })
        self.assertEqual(movie_models.Movie.objects.count(),1)


    def test_create_show(self):
        """     Test Create Show API    """
        response = self.client.post('/movie/create-movie',
            movie_1, format='json')
        response = self.client.post('/movie/create-movie-show',
            movie_show_1, format='json')

        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, {
            "id":1,
            "movie": 1,
            "start_time": "13:00:00",
            "screen_number":1
        })
        self.assertEqual(
            (movie_models.MovieShow.objects.filter(
                movie__pk=1).count()),1)

    def test_update_show_timing(self):
        """     Test Update Show Timing API    """
        response = self.client.post('/movie/create-movie',
            movie_1, format='json')
        response = self.client.post('/movie/create-movie-show',
            movie_show_1, format='json')
        response = self.client.put('/movie/update-movie-show/1',
            new_timimg_movie_show_1, format='json')

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {
            "id":1,
            "movie": 1,
            "start_time": "15:00:00",
            "screen_number":1
        })
        self.assertEqual(
            (movie_models.MovieShow.objects.filter(
                movie__pk=1).count()),1)

    def test_get_shows_at_particular_time(self):
        """     Test Get Shows At Particular Time API   """
        response = self.client.post('/movie/create-movie',
            movie_1, format='json')
        response = self.client.post('/movie/create-movie',
            movie_2, format='json')
        response = self.client.post('/movie/create-movie-show',
            movie_show_1, format='json')
        response = self.client.post('/movie/create-movie-show',
            movie_show_2, format='json')
        response = self.client.get(
            '/movie/get-movies-shows?start_time=13:00:00',
            format='json')

        self.assertEqual(
            response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content), [{
                "id":1,
                "movie": {
                    "id":1,
                    "name":"Race",
                    "description":"Bollywood Thriller/Action Movie",
                    "language":"Hindi",
                    "director":"Abbas Burmawalla",
                    "cast":"Saif Ali Khan, Akshaye Khanna, Katrina Kaif",
                    "duration_min":125
                },
                "start_time":"13:00:00",
                "screen_number":1
            }, {
            "id":2,
            "movie": {
                "id":2,
                "name":"The Fate of the Furious",
                "description":"Hollywood Thriller/Action Movie",
                "language":"English",
                "director":"F. Gary Gray",
                "cast":"Vin Diesel, Dwayne Johnson, Jason Statham",
                "duration_min":125
            },
            "start_time":"13:00:00",
            "screen_number":1
        }])
