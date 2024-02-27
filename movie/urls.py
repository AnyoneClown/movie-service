from django.urls import path
from movie.views import DirectorListView, DirectorDetailView, ActorListView, ActorDetailView, MovieListView, MovieDetailView

urlpatterns = [
    path("directors/", DirectorListView.as_view(), name="director-list"),
    path("directors/<int:pk>/", DirectorDetailView.as_view(), name="director-detail"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
]

app_name = "movies"
