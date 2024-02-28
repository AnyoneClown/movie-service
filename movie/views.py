from rest_framework import generics, viewsets

from movie.models import Director, Actor, Movie
from movie.serializers import DirectorSerializer, ActorSerializer, MovieSerializer, MovieDetailSerializer


class DirectorViewSet(viewsets.ModelViewSet):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filterset_fields = ["first_name", "last_name"]


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filterset_fields = ["first_name", "last_name"]


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.prefetch_related("actors").select_related("director")
    serializer_class = MovieSerializer
    filterset_fields = [
        "year",
        "actors__first_name",
        "actors__last_name",
        "director__first_name",
        "director__last_name",
    ]

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MovieDetailSerializer
        return self.serializer_class
