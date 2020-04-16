from unittest.mock import patch

from moviewarehouse.movies.models import Comment, Movie
from moviewarehouse.movies.tests.factories import (
    CommentFactory,
    MovieFactory,
    mocked_movie_data,
    mocked_movie_full_data,
    mocked_movie_not_found,
)
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class MovieViewSetTest(APITestCase):
    def setUp(self):
        self.movie1 = MovieFactory()
        self.movie2 = MovieFactory()
        self.movie3 = MovieFactory()

        self.base_url = reverse("movie-list")

    def test_get_listing(self):
        response = self.client.get(self.base_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 3)

    def test_get_filtering(self):
        movie = MovieFactory(title="r3t45hrgfew32r4")
        response = self.client.get(f"{self.base_url}?title__iexact={movie.title}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    @patch("requests.get", return_value=mocked_movie_data())
    def test_post_create_movie(self, mocked_movie_data):
        title = mocked_movie_data().json_data["Title"]

        response = self.client.post(self.base_url, data={"title": title})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], title)
        self.assertEqual(Movie.objects.count(), 4)

        response = self.client.post(self.base_url, data={"title": title})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], title)
        self.assertEqual(Movie.objects.count(), 4)

    @patch("requests.get", return_value=mocked_movie_full_data())
    def test_post_create_movie_full_data(self, mocked_movie_full_data):
        title = mocked_movie_full_data().json_data["Title"]
        response = self.client.post(self.base_url, data={"title": title})

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], title)
        self.assertEqual(Movie.objects.count(), 4)

        response = self.client.post(self.base_url, data={"title": title})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], title)
        self.assertEqual(Movie.objects.count(), 4)

    @patch("requests.get", return_value=mocked_movie_not_found())
    def test_post_create_not_found(self, mocked_movie_not_found):
        title = "12r32t43g"
        response = self.client.post(self.base_url, data={"title": title})

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(Movie.objects.count(), 3)


class CommentViewSetTest(APITestCase):
    def setUp(self):
        self.comment1 = CommentFactory()
        self.comment2 = CommentFactory()
        self.comment3 = CommentFactory()

        self.base_url = reverse("comment-list")

    def test_get_listing(self):
        response = self.client.get(self.base_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 3)

    def test_get_filtering(self):
        comment = CommentFactory()
        response = self.client.get(f"{self.base_url}?movie_id={comment.movie_id}")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_post_create_comment(self):
        movie = MovieFactory()
        body = "Test body"

        response = self.client.post(
            self.base_url, data={"body": body, "movie": movie.id}
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["body"], body)
        self.assertEqual(Comment.objects.count(), 4)
