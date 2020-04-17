from django.db.models import Count, F, Q, Window
from django.db.models.functions.window import DenseRank
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status as rest_status
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from moviewarehouse.movies.filters import MovieFilter
from moviewarehouse.movies.models import Comment, Movie
from moviewarehouse.movies.serializers import (
    CommentSerializer,
    MovieSearchSerializer,
    MovieSerializer,
    TopMovieSearchSerializer,
    TopMovieSerializer,
)
from moviewarehouse.movies.utils import get_movie_details


class TopMovieViewSet(ListModelMixin, GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = TopMovieSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        serializer = TopMovieSearchSerializer(data=self.request.GET)
        serializer.is_valid(raise_exception=True)

        queryset = queryset.annotate(
            total_comments=Count(
                "comments",
                filter=Q(
                    comments__created_at__range=[
                        serializer.data["date_from"],
                        serializer.data["date_to"],
                    ]
                ),
            ),
            rank=Window(expression=DenseRank(), order_by=F("total_comments").desc()),
        )

        return queryset


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
