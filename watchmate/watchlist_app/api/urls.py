from django.urls import path
from watchlist_app.api.views import MovieDetailAV, MovieListAV

urlpatterns = [
    path('list/', MovieListAV.as_view(), name='movie_list'),
    path('<int:movie_id>', MovieDetailAV.as_view(), name='movie')
]