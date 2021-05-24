from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as authViews


urlpatterns = [
    path('', views.index, name = 'index'),
    path('admin/', admin.site.urls),
    # path('<int:film_id>/', views.film, name = 'films'),
    # path('<str:genre_str>/',views.genre, name = 'genre'),
    # path('<str:genre_str>/<int:film_id>',views.film, name = 'films'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('podpiska/', views.podpiska, name='podpiska'),
    path('serials/', views.serials, name='serials'),
    path('films/', views.films, name='films'),
    path('notfound/', views.notfound, name='notfound'),
    path('cabinet/', views.cabinet, name='cabinet'),
    path('filmPage/', views.filmPage, name='filmPage'),
    path('exit/', authViews.LogoutView.as_view(
        next_page='/'), name='exit'),
]