from rest_framework import serializers
from movie.models import Director, Actor, Movie


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ("id", "first_name", "last_name")


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ("id", "first_name", "last_name")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("id", "title", "year", "director", "actors")


class MovieDetailSerializer(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ("id", "title", "year", "director", "actors")
