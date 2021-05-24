from django.contrib import admin
from .models import Model_for_storing_movies_from_the_main_page, \
                    Model_for_storing_movies_from_the_film_page, \
                    Model_for_storing_series, Model_for_storing_genres




@admin.register(Model_for_storing_movies_from_the_main_page)
class Model_for_storing_movies_from_the_main_pageAdmin(admin.ModelAdmin):
    """
    
    
    
    """
    list_display = (
        'movie_title', 
        'movie_genre', 
        'movie_raiting', 
        'movie_date_release', 
        'movie_age_limit')

    list_filter = (
        'movie_genre', 
        'movie_raiting', 
        'movie_date_release', 
        'movie_age_limit')

    search_fields = (
        'movie_title', 
        'movie_genre')

@admin.register(Model_for_storing_movies_from_the_film_page)
class Model_for_storing_movies_from_the_film_pageAdmin(admin.ModelAdmin):
    """
    
    
    
    """    
    list_display = (
        'movie_title', 
        'movie_genre', 
        'movie_raiting', 
        'movie_date_release', 
        'movie_age_limit')

    list_filter = (
        'movie_genre', 
        'movie_raiting', 
        'movie_date_release', 
        'movie_age_limit')

    search_fields = (
        'movie_title', 
        'movie_genre')

admin.site.register(Model_for_storing_genres)

@admin.register(Model_for_storing_series)
class Model_for_storing_seriesAdmin(admin.ModelAdmin):
    """
    
    
    
    """
    list_display = (
        'movie_title', 
        'movie_genre', 
        'movie_raiting', 
        'movie_date_release', 
        'movie_age_limit')

    list_filter = (
        'movie_genre', 
        'movie_raiting', 
        'movie_date_release', 
        'movie_age_limit')

    search_fields = (
        'movie_title', 
        'movie_genre')