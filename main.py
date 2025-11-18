from fastapi import FastAPI
from pathlib import Path
import csv

app = FastAPI()

# Ścieżka do folderu z danymi
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "database"


# ===== MODELE DANYCH (zwykłe klasy) =====

class Movie:
    def __init__(self, movie_id: int, title: str, genres: str):
        self.id = movie_id
        self.title = title
        self.genres = genres


class Link:
    def __init__(self, movie_id: int, imdb_id: str, tmdb_id: str | None):
        self.movie_id = movie_id
        self.imdb_id = imdb_id
        self.tmdb_id = tmdb_id


class Rating:
    def __init__(self, user_id: int, movie_id: int, rating: float, timestamp: int):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp


class Tag:
    def __init__(self, user_id: int, movie_id: int, tag: str, timestamp: int):
        self.user_id = user_id
        self.movie_id = movie_id
        self.tag = tag
        self.timestamp = timestamp


# ===== 1. Prosty endpoint hello world =====

@app.get("/")
def hello_world():
    return {"hello": "world"}


# ===== Funkcje pomocnicze do wczytywania CSV =====

def load_movies() -> list[Movie]:
    movies: list[Movie] = []
    with (DATA_DIR / "movies.csv").open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies.append(
                Movie(
                    movie_id=int(row["movieId"]),
                    title=row["title"],
                    genres=row["genres"],
                )
            )
    return movies


def load_links() -> list[Link]:
    links: list[Link] = []
    with (DATA_DIR / "links.csv").open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            links.append(
                Link(
                    movie_id=int(row["movieId"]),
                    imdb_id=row["imdbId"],
                    tmdb_id=row.get("tmdbId") or None,
                )
            )
    return links


def load_ratings() -> list[Rating]:
    ratings: list[Rating] = []
    with (DATA_DIR / "ratings.csv").open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            ratings.append(
                Rating(
                    user_id=int(row["userId"]),
                    movie_id=int(row["movieId"]),
                    rating=float(row["rating"]),
                    timestamp=int(row["timestamp"]),
                )
            )
    return ratings


def load_tags() -> list[Tag]:
    tags: list[Tag] = []
    with (DATA_DIR / "tags.csv").open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tags.append(
                Tag(
                    user_id=int(row["userId"]),
                    movie_id=int(row["movieId"]),
                    tag=row["tag"],
                    timestamp=int(row["timestamp"]),
                )
            )
    return tags


# ===== ENDPOINTY – używamy __dict__ do serializacji =====

@app.get("/movies")
def get_movies():
    movies = load_movies()
    return [m.__dict__ for m in movies]


@app.get("/links")
def get_links():
    links = load_links()
    return [l.__dict__ for l in links]


@app.get("/ratings")
def get_ratings():
    ratings = load_ratings()
    return [r.__dict__ for r in ratings]


@app.get("/tags")
def get_tags():
    tags = load_tags()
    return [t.__dict__ for t in tags]
