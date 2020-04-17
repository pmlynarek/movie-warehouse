from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext as _

from moviewarehouse.movies.choices import RatingChoices


class Movie(models.Model):
    imdb_id = models.CharField(_("imdb id"), max_length=50)

    title = models.CharField(_("title"), max_length=255, unique=True)
    plot = models.TextField(_("plot"), blank=True)

    year = models.PositiveSmallIntegerField(_("year"), blank=True, null=True)
    runtime = models.PositiveSmallIntegerField(_("runtime"), blank=True, null=True)
    released = models.DateField(_("released"), blank=True, null=True)
    dvd = models.DateField(_("dvd"), blank=True, null=True)

    pg_rating = models.CharField(
        _("pg rating"), max_length=10, blank=True, choices=RatingChoices.choices
    )
    rating = models.DecimalField(_("rating"), max_digits=2, decimal_places=1, null=True)

    genre = models.CharField(_("genre"), max_length=100, blank=True)

    language = models.CharField(_("language"), max_length=100, blank=True)
    country = models.CharField(_("country"), max_length=100, blank=True)

    director = models.CharField(_("director"), max_length=255, blank=True)
    writer = models.TextField(_("writer"), blank=True)
    actors = models.CharField(_("actors"), max_length=255, blank=True)

    awards = models.CharField(_("awards"), max_length=255, blank=True)
    poster = models.URLField(_("poster"), max_length=255, blank=True)
    production = models.CharField(_("production"), max_length=100, blank=True)

    website = models.URLField(_("website"), blank=True)

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    movie = models.ForeignKey(
        Movie,
        verbose_name=_("movie"),
        related_name="comments",
        on_delete=models.CASCADE,
    )
    body = models.TextField(_("body"))
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)

    def __str__(self):
        return truncatechars(self.body, 160)
