from factory import Faker, SubFactory, django
from rest_framework import status


class MovieFactory(django.DjangoModelFactory):
    class Meta:
        model = "movies.Movie"

    title = Faker("uuid4")
    imdb_id = Faker("uuid4")
    plot = Faker("word")
    year = Faker("random_int")
    runtime = Faker("random_int")
    released = Faker("date")
    dvd = Faker("date")
    pg_rating = "NC-17"
    rating = Faker("random_digit")
    genre = Faker("word")
    language = Faker("word")
    country = Faker("word")
    director = Faker("word")
    writer = Faker("word")
    actors = Faker("word")
    awards = Faker("word")
    production = Faker("word")
    website = Faker("url")


class CommentFactory(django.DjangoModelFactory):
    class Meta:
        model = "movies.Comment"

    body = Faker("word")
    movie = SubFactory(MovieFactory)


class MockResponse:
    def __init__(self, json_data, status_code, **kwargs):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

    @property
    def ok(self):
        return True


def mocked_movie_data(**kargs):
    return MockResponse(
        json_data={
            "Title": "Netflix",
            "Year": "2014",
            "Rated": "N/A",
            "Released": "09 Jun 2014",
            "Runtime": "N/A",
            "Genre": "Short, Comedy",
            "Director": "Chris McMillan",
            "Writer": "Van Corona",
            "Actors": "Kasey Dailey",
            "Plot": "Netflix and chill Netflix and chill Netflix and chill Netflix and chill Netflix and chill Netflix and chill Netflix and chill Netflix and chill",
            "Language": "English",
            "Country": "USA",
            "Awards": "N/A",
            "Poster": "N/A",
            "Ratings": [{"Source": "Internet Movie Database", "Value": "6.8/10"}],
            "Metascore": "N/A",
            "imdbRating": "6.8",
            "imdbVotes": "26",
            "imdbID": "tt3816512",
            "Type": "movie",
            "DVD": "N/A",
            "BoxOffice": "N/A",
            "Production": "N/A",
            "Website": "N/A",
            "Response": "True",
        },
        status_code=status.HTTP_200_OK,
    )


def mocked_movie_full_data(**kargs):
    return MockResponse(
        json_data={
            "Title": "Titanic",
            "Year": "1997",
            "Rated": "PG-13",
            "Released": "19 Dec 1997",
            "Runtime": "194 min",
            "Genre": "Drama, Romance",
            "Director": "James Cameron",
            "Writer": "James Cameron",
            "Actors": "Leonardo DiCaprio, Kate Winslet, Billy Zane, Kathy Bates",
            "Plot": "A seventeen-year-old aristocrat falls in love with a kind but poor artist aboard the luxurious, ill-fated R.M.S. Titanic.",
            "Language": "English, Swedish, Italian",
            "Country": "USA",
            "Awards": "Won 11 Oscars. Another 114 wins & 83 nominations.",
            "Poster": "https://m.media-amazon.com/images/M/MV5BMDdmZGU3NDQtY2E5My00ZTliLWIzOTUtMTY4ZGI1YjdiNjk3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_SX300.jpg",
            "Ratings": [
                {"Source": "Internet Movie Database", "Value": "7.8/10"},
                {"Source": "Rotten Tomatoes", "Value": "89%"},
                {"Source": "Metacritic", "Value": "75/100"},
            ],
            "Metascore": "75",
            "imdbRating": "7.8",
            "imdbVotes": "997,454",
            "imdbID": "tt0120338",
            "Type": "movie",
            "DVD": "10 Sep 2012",
            "BoxOffice": "N/A",
            "Production": "Paramount Pictures",
            "Website": "http://www.example.com",
            "Response": "True",
        },
        status_code=status.HTTP_200_OK,
    )


def mocked_movie_not_found(**kargs):
    return MockResponse(
        json_data={"Response": "False", "Error": "Movie not found!"},
        status_code=status.HTTP_200_OK,
    )
