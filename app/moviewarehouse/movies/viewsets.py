from django_filters.rest_framework import DjangoFilterBackend
from moviewarehouse.movies.filters import MovieFilter
from moviewarehouse.movies.models import Comment, Movie
from moviewarehouse.movies.serializers import (
    CommentSerializer,
    MovieSearchSerializer,
    MovieSerializer,
)
from moviewarehouse.movies.utils import get_movie_details
from rest_framework import status as rest_status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet


class MovieViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = MovieFilter

    def create(self, request, *args, **kwargs):
        serializer_search = MovieSearchSerializer(data=request.data)
        serializer_search.is_valid(raise_exception=True)

        data, status = get_movie_details(serializer_search.data["title"])

        if not data or status == rest_status.HTTP_404_NOT_FOUND:
            return Response({}, status=status)

        headers = self.get_success_headers(data)
        return Response(data, status=status, headers=headers)


class CommentViewSet(ListModelMixin, CreateModelMixin, GenericViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("movie_id",)
