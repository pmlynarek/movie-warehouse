from django.contrib import admin
from django.urls import path
from moviewarehouse.movies.viewsets import CommentViewSet, MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")
router.register(r"comments", CommentViewSet, basename="comment")


urlpatterns = [path("admin/", admin.site.urls)]
urlpatterns += router.urls
