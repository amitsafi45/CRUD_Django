
from django.urls import path
from .views import Movies
urlpatterns=[
    path('movie/',Movies.as_view(),name='get-list'),
    path('movie/<int:pk>/',Movies.as_view(),name='get-data-by-id')
]