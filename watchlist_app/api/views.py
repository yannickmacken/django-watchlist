from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer


class MovieListAV(APIView):
    
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # serializer.save() calls create() or update() on serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MovieDetailAV(APIView):
    
    def get(self, request, movie_id):  # request passed as arg, movie id as kwarg
        movie, response = self._get_movie(movie_id)
        if not movie:
            return response
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, movie_id):
        movie, response = self._get_movie(movie_id)
        if not movie:
            return response
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, movie_id):
        movie, response = self._get_movie(movie_id)
        if not movie:
            return response
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    ### HELPERS ###

    def _get_movie(movie_id: int):
        movie = None
        response = None
        try:
            movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            response = Response({'Error', f'movie with id {movie_id} not found'}, status=status.HTTP_404_NOT_FOUND)
        return (movie, response)