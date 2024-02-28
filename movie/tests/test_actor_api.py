from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from movie.models import Actor
from movie.serializers import ActorSerializer


class TestActorViews(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_list_actors(self):
        Actor.objects.create(first_name="John", last_name="Doe")
        Actor.objects.create(first_name="Jane", last_name="Smith")

        response = self.client.get(reverse("movies:actor-list"))
        actors = Actor.objects.all()
        serializer = ActorSerializer(actors, many=True)

        paginated_response_data = response.data.get("results", [])

        self.assertEqual(response.data["count"], len(serializer.data))
        self.assertEqual(paginated_response_data, serializer.data)

    def test_detail_actor(self):
        actor = Actor.objects.create(first_name="John", last_name="Doe")

        response = self.client.get(reverse("movies:actor-detail", kwargs={"pk": actor.pk}))
        serializer = ActorSerializer(instance=actor)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_actors(self):
        Actor.objects.create(first_name="John", last_name="Doe")
        Actor.objects.create(first_name="Jane", last_name="Smith")

        response = self.client.get(reverse("movies:actor-list"), {"last_name": "Doe"})
        actors = Actor.objects.filter(last_name="Doe")
        serializer = ActorSerializer(actors, many=True)

        paginated_response_data = response.data.get("results", [])

        self.assertEqual(response.data["count"], len(serializer.data))
        self.assertEqual(paginated_response_data, serializer.data)
