import logging
from typing import Tuple, Union

import requests
from django.conf import settings
from rest_framework import status

from moviewarehouse.movies.models import Movie
from moviewarehouse.movies.serializers import MovieSerializer

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def get_movie_data_by_title(title: str) -> Union[dict, None]:
    try:
        movie = Movie.objects.get(title__iexact=title)
        return MovieSerializer(instance=movie).data
    except Movie.DoesNotExist:
        pass


def get_movie_details(title: str) -> Tuple[dict, int]:
    # Check if movie already exists in database
    if data:=get_movie_data_by_title(title): return data, status.HTTP_200_OK

    # Get movie data - searching by title
    try:
        response = requests.get(
            settings.OMDB_API_URL.format(apikey=settings.OMDB_API_KEY, title=title),
            timeout=2,
        )
        omdb_data = response.json()
    except Exception as e:
        logger.error(
            f"Error during fetching data about movie. Title: {title}, exception: {e}"
        )
        return {}, status.HTTP_404_NOT_FOUND

    # Check if movie data was returned
    if not response.ok or omdb_data.get("Response") == "False":
        return {}, status.HTTP_404_NOT_FOUND

    # Check if movie already exists in database - using returned title
    if data:=get_movie_data_by_title(omdb_data.get("Title")): return data, status.HTTP_200_OK

    # Create and return movie
    data = map_movie_data(omdb_data)
    serializer = MovieSerializer(data=data)

    if not serializer.is_valid():
        logger.warning(f"Serializer validation errors: {serializer.errors}")
        return {}, status.HTTP_404_NOT_FOUND

    try:
        serializer.save()
        return serializer.data, status.HTTP_201_CREATED
    except Exception as e:
        logger.error(f"Error during saving draft movie. Title: {title}, exception: {e}")
    return {}, status.HTTP_404_NOT_FOUND


def map_movie_data(data: dict) -> dict:
    for key in data.keys():
        if data.get(key) and data[key] == "N/A":
            data[key] = ""

    return {
        "imdb_id": data.get("imdbID", ""),
        "title": data.get("Title", ""),
        "plot": data.get("Plot", ""),
        "year": data["Year"] if data.get("Year") else None,
        "runtime": data["Runtime"] if data.get("Runtime") else None,
        "released": data["Released"] if data.get("Released") else None,
        "dvd": data["DVD"] if data.get("DVD") else None,
        "pg_rating": data.get("Rated", ""),
        "rating": data.get("imdbRating"),
        "genre": data.get("Genre", ""),
        "language": data.get("Language", ""),
        "country": data.get("Country", ""),
        "director": data.get("Director", ""),
        "writer": data.get("Writer", ""),
        "actors": data.get("Actors", ""),
        "awards": data.get("Awards", ""),
        "poster": data.get("Poster", ""),
        "production": data.get("Production", ""),
        "website": data.get("Website", ""),
    }
