from typing import Any, Callable, List, Optional, Union
from django.urls import path
from apps.movies.views import (
    TagViewSet,
    TagCreateViewSet,
    TaggedMovieList,
    MovieList,
    MovieDetail,
    MovieCreateView,
    MovieUpdateView,
    )
# Create your views here.

urlpatterns: List[Union[str, Callable[..., Any], Optional[str]]] = [
    path('tag/create/', TagCreateViewSet.as_view(), name='tag-create'),
    path('tag/<str:tag>/', TaggedMovieList.as_view(), name='tagged-movie-list'),
    path('tags/', TagViewSet.as_view({'get': 'list'}), name='tags'),
    path('list/', MovieList.as_view(), name='movie-list'),
    path('create/', MovieCreateView.as_view(), name='movie-create'),
    path('update/<int:pk>/', MovieUpdateView.as_view(), name='movie-update'),
    path('detail/<int:pk>/', MovieDetail.as_view(), name='movie-detail'),
]