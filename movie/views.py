from rest_framework import generics

from movie.models import Director, Actor, Movie
from movie.serializers import DirectorSerializer, ActorSerializer, MovieSerializer, MovieDetailSerializer


class DirectorListView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer
    filterset_fields = ["first_name", "last_name"]

class DirectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ActorListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    filterset_fields = ["first_name", "last_name"]


class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.prefetch_related("actors").select_related("director")
    serializer_class = MovieSerializer
    filterset_fields = ["year", "actors__first_name", "actors__last_name", "director__first_name", "director__last_name",]

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieDetailSerializer
        return self.serializer_class


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.prefetch_related("actors").select_related("director")
    serializer_class = MovieSerializer

    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieDetailSerializer
        return self.serializer_class
