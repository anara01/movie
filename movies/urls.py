from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MoviesView.as_view()),
    path("filter/", FilterMovieView.as_view(), name='filter'),
    path("add-rating/", AddStarRating.as_view(), name='add_rating'),
    path("json-filter/", JsonFilterMoviesView.as_view(), name='json_filter'),
    path("<slug:slug>/", MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", AddReview.as_view(), name='add_review'),
    path("actor/<str:slug>/", ActorView.as_view(), name='actor_detail'),
]