from django.db import models


class Director(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self) -> str:
        """Returns the full name of the Director."""
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name"]
        verbose_name = "Director"
        verbose_name_plural = "Directors"
        app_label = "movie"
        db_table = "directors"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Actor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def full_name(self) -> str:
        """Returns the full name of the actor."""
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["first_name"]
        verbose_name = "Actor"
        verbose_name_plural = "Actors"
        app_label = "movie"
        db_table = "actors"

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_NULL, related_name="movies", null=True)
    actors = models.ManyToManyField(Actor, related_name="movies")

    class Meta:
        ordering = ["title"]
        verbose_name = "Movie"
        verbose_name_plural = "Movies"
        app_label = "movie"
        db_table = "movies"

    def __str__(self) -> str:
        return (
            f"Title: {self.title}, Year: {self.year} Director: {self.director.full_name}, "
            f"Actors: {', '.join([actor.full_name for actor in self.actors.all()])}"
        )
