from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
    path('', 
        views.index, 
        name = 'index'),

    path('admin/',
        admin.site.urls,
        name='admin'),

    path('accounts/', 
        include('django.contrib.auth.urls'),
        name='accounts'),

    path('podpiska/', 
        views.podpiska, 
        name='podpiska'),

    path('serials/', 
        views.serials, 
        name='serials'),

    path('films/', 
        views.films, 
        name='films'),

    path('notfound/', 
        views.notfound, 
        name='notfound'),

    path('cabinet/', 
        views.cabinet, 
        name='cabinet'),

    path('genrePage/<int:genre_id>', 
        views.movies_by_genre, 
        name = 'genrePage'),

    path('filmPage/', 
        views.search, 
        name='filmPage'),

    path('filmPage/<str:movie_title>/<int:film_id>/', 
        views.film, 
        name = 'films'),

    path('exit/', 
        authViews.LogoutView.as_view(
        next_page='/'), 
        name='exit'),
]