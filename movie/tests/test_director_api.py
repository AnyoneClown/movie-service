from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from movie.models import Director
from movie.serializers import DirectorSerializer


class TestDirectorViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_detail_director(self):
        director = Director.objects.create(first_name="John", last_name="Doe")

        response = self.client.get(reverse("movies:director-detail", kwargs={"pk": director.pk}))
        serializer = DirectorSerializer(instance=director)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_list_directors(self):
        Director.objects.create(first_name="John", last_name="Doe")
        Director.objects.create(first_name="Jane", last_name="Smith")

        response = self.client.get(reverse("movies:director-list"))
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)

        paginated_response_data = response.data.get("results", [])

        self.assertEqual(response.data["count"], len(serializer.data))
        self.assertEqual(paginated_response_data, serializer.data)

    def test_filter_directors(self):
        Director.objects.create(first_name="John", last_name="Doe")
        Director.objects.create(first_name="Jane", last_name="Smith")

        response = self.client.get(reverse("movies:director-list"), {"last_name": "Doe"})
        directors = Director.objects.filter(last_name="Doe")
        serializer = DirectorSerializer(directors, many=True)

        paginated_response_data = response.data.get("results", [])

        self.assertEqual(response.data["count"], len(serializer.data))
        self.assertEqual(paginated_response_data, serializer.data)
