from django.urls import path
from watchlist_app.views import movie_list
from watchlist_app.views import movie_details

urlpatterns = [
    path('list/', movie_list, name='movie_list'),
    path('<int:movie_id>', movie_details, name='movie')
]