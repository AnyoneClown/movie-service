import requests

from typing import NoReturn
from bs4 import BeautifulSoup

from movie.models import Movie, Director, Actor
from movie_service.settings import IMDB_API_URL, API_KEY


IMDB_MOVIE_URL = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


def load_movies_data(movie_id: str) -> NoReturn:
    url = f"{IMDB_API_URL}?apikey={API_KEY}&i={movie_id}"

    data = requests.get(url).json()

    title = data.get("Title")
    year = int(data.get("Year"))
    director_name = data.get("Director")
    actors_names = data.get("Actors").split(", ")

    director, _ = Director.objects.get_or_create(
        first_name=director_name.split()[0], last_name=director_name.split()[1]
    )

    movie, _ = Movie.objects.get_or_create(title=title, year=year, director=director)

    for actor_name in actors_names:
        actor_parts = actor_name.split()

        if len(actor_parts) == 1:
            continue

        if len(actor_parts) == 3:
            first_name = actor_parts[0]
            last_name = actor_parts[2]
        else:
            first_name, last_name = actor_parts

        actor, _ = Actor.objects.get_or_create(first_name=first_name, last_name=last_name)

        movie.actors.add(actor)


def scrape_imdb() -> list[str]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    response = requests.get(IMDB_MOVIE_URL, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    movie_ids = []
    movie_links = soup.find_all("a", class_="ipc-title-link-wrapper")

    for link in movie_links:
        href = link.get("href")
        movie_id = href.split("/")[2]
        movie_ids.append(movie_id)

    return movie_ids[:250]


def main() -> NoReturn:
    movie_ids = scrape_imdb()

    for movie_id in movie_ids:
        load_movies_data(movie_id)
