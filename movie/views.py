from rest_framework import generics

from movie.models import Director, Actor, Movie
from movie.serializers import DirectorSerializer, ActorSerializer, MovieSerializer, MovieDetailSerializer


class DirectorListView(generics.ListCreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class DirectorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer


class ActorListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class ActorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.prefetch_related("actors").select_related("director")
    serializer_class = MovieSerializer

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
