from rest_framework.decorators import api_view
from rest_framework.response import Response
from watchlist_app.api.serializers import MovieSerializer
from watchlist_app.models import Movie

# Create your views here.

@api_view()
def movieList(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view()
def movieDetails(request, pk):
    movie = Movie.objects.get(pk=pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)







