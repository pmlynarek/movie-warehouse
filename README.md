# Welcome to movie-warehouse

Simple test application to storing and looking for data about movies. You can also add some comments to your downloaded movies and get top movies(ranking is determined by count of comments).

## Requirements

* Docker
* Docker Compose

## Setup
* Clone the repository
* Go to project directory
* mv example.env to .env and replace `xxx` values for your own(OMDB_API_KEY you can get from http://www.omdbapi.com/)
* make up

## Quickstart guide

Start the project:

    make up

Bring project down:

    make down

To test the project run:

    make test

To build project:

    make build

## Documentation

You can easily review all endpoints using these links:

* /swagger/ - http://localhost:8000/swagger/
* /redoc/ - http://localhost:8000/redoc/

### Local testing - example requests:
* POST - http://localhost:8000/movies/ - BODY {"title": "Avatar"}
* GET - http://localhost:8000/movies/?title__icontains=avatar
* GET - http://localhost:8000/comments/?movie_id=20
* POST - http://localhost:8000/comments/ -  BODY {"body": "Test", "movie": 1}
* GET - http://localhost:8000/top/?date_from=2020-01-01&date_to=2020-04-20

### Additional packages

* django-choices - Choices are much cleaner, than standard - some additional functions
* factory-boy - Transparent fixtures, speeding up writing tests
* drf-yasg - Complex documentation without any effor
