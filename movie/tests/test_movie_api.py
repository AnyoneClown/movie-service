from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from movie.models import Movie, Director
from movie.serializers import MovieDetailSerializer


class TestMovieViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_movies(self):
        director = Director.objects.create(first_name="John", last_name="Doe")
        Movie.objects.create(title="Movie 1", year=2020, director=director)
        Movie.objects.create(title="Movie 2", year=2021, director=director)

        response = self.client.get(reverse("movies:movie-list"))
        movies = Movie.objects.all()
        serializer = MovieDetailSerializer(movies, many=True)

        paginated_response_data = response.data.get("results", [])

        self.assertEqual(response.data["count"], len(serializer.data))
        self.assertEqual(paginated_response_data, serializer.data)

    def test_detail_movie(self):
        director = Director.objects.create(first_name="John", last_name="Doe")
        movie = Movie.objects.create(title="Movie 1", year=2020, director=director)

        response = self.client.get(reverse("movies:movie-detail", kwargs={"pk": movie.pk}))
        serializer = MovieDetailSerializer(instance=movie)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_movies(self):
        director = Director.objects.create(first_name="John", last_name="Doe")
        Movie.objects.create(title="Movie 1", year=2020, director=director)
        Movie.objects.create(title="Movie 2", year=2021, director=director)

        response = self.client.get(reverse("movies:movie-list"), {"year": 2020})
        movies = Movie.objects.filter(year=2020)
        serializer = MovieDetailSerializer(movies, many=True)

        paginated_response_data = response.data.get("results", [])

        self.assertEqual(response.data["count"], len(serializer.data))
        self.assertEqual(paginated_response_data, serializer.data)
