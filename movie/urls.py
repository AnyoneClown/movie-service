from rest_framework import routers

from movie.views import MovieViewSet, DirectorViewSet, ActorViewSet

router = routers.DefaultRouter()
router.register("movies", MovieViewSet)
router.register("directors", DirectorViewSet)
router.register("actors", ActorViewSet)

urlpatterns = router.urls

app_name = "movies"
