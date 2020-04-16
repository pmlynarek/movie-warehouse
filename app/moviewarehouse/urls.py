from django.contrib import admin
from django.urls import path
from moviewarehouse.movies.viewsets import MovieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"movies", MovieViewSet, basename="movie")


urlpatterns = [path("admin/", admin.site.urls)]
urlpatterns += router.urls
