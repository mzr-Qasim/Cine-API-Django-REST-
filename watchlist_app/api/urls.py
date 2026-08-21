from django.urls import path, include
from watchlist_app.api.views import MovieListAV, MovieDetailAV, MovieAiAV


urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie-list'),
    path('<int:pk>/', MovieDetailAV.as_view(), name='movie-detail'),  
    path("<int:pk>/ai-review/", MovieAiAV.as_view(), name="movie-ai-review")
    
]




