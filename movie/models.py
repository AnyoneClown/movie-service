from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, related_name="movies", null=True)
    actors = models.ManyToManyField(Actor, related_name="movies")

    def __str__(self) -> str:
        return f"Title: {self.title}, Year: {self.year}"
