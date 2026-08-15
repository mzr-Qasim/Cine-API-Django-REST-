from django.urls import path
from watchlist_app.views import movieList, movieDetails


urlpatterns = [
    path('list/', movieList, name='movie-list'),
    path('<int:pk>', movieDetails, name='movie-detail'),
]
