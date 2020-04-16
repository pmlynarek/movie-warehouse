from django_filters import rest_framework as filters
from moviewarehouse.movies.models import Movie


class MovieFilter(filters.FilterSet):
    class Meta:
        model = Movie
        fields = {
            "title": ["iexact", "icontains"],
            "imdb_id": ["iexact", "exact"],
            "rating": ["lt", "lte", "gt", "gte"],
            "pg_rating": ["iexact", "exact"],
            "year": ["lt", "lte", "gt", "gte"],
            "runtime": ["lt", "lte", "gt", "gte"],
            "released": ["lt", "lte", "gt", "gte"],
            "dvd": ["lt", "lte", "gt", "gte"],
        }
