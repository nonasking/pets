from django.urls import path

from movies.views import ActorsView, MoviesView

app_name = 'movies'

urlpatterns = [
    path('/actors/', ActorsView.as_view()),
    path('/movies/', MoviesView.as_view()),
]


