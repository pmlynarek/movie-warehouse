from django.contrib import admin
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext as _
from moviewarehouse.movies.models import Comment, Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")


admin.site.register(Movie, MovieAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "get_body")

    def get_body(self, instance):
        return truncatechars(instance.body, 30)

    get_body.short_description = _("body")


admin.site.register(Comment, CommentAdmin)
