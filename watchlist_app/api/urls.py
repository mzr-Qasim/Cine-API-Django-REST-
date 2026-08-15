from django.urls import path, include
from watchlist_app.api.views import movieList, movieDetails


urlpatterns = [
    path('list/', movieList, name='movie-list'),
    path('<int:pk>/', movieDetails, name='movie-detail')    
    
]