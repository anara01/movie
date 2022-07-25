from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MoviesView.as_view()),
    path("<slug:slug>/", MovieDetailView.as_view(), name='movie_detail'),
]