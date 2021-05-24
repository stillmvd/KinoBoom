from django.db import models

class Model_for_storing_movies_from_the_main_page(models.Model):
    """Creates a model for storing movie data

    * move_title - This field will store the name of the movie
    
    * movie_description - This field will store the description of the movie

    * movie_genre - This field will store the genre of the movie

    * movie_raiting - This field will store the rating of the movie

    * movie_date_release - This field will store the release date of the movie

    * movie_age_limit - This field will store the age limit for the movie

    * path_to_the_image - This field will store the path to the photo to the movie
    """

    movie_title = models.CharField(
        max_length=30,
        verbose_name="Название фильма")

    movie_description = models.TextField(
        verbose_name="Описание")

    movie_genre = models.ForeignKey(
        'Model_for_storing_genres', 
        on_delete = models.PROTECT, 
        verbose_name="Жанр")
    
    movie_raiting = models.CharField(
        max_length=5, 
        verbose_name="Рейтинг")

    movie_date_release = models.CharField(
        max_length=20, 
        verbose_name="Дата выхода")

    movie_age_limit = models.CharField(
        max_length=10, 
        verbose_name="Возрастное ограничение")

    path_to_the_image = models.ImageField(
        upload_to='img/', 
        verbose_name="file")

    def __str__(self) -> str:
        """
        When accessing the class, returns the name of the Movie
        """
        return self.movie_title
    
    class Meta:
        """
        How it will be displayed in the django admin panel
        """
        verbose_name = "Фильм на главной страничке"
        verbose_name_plural = "Фильмы на главной страничке"

class Model_for_storing_movies_from_the_film_page(models.Model):
    """Creates a model for storing movie data

    * move_title - This field will store the name of the movie
    
    * movie_description - This field will store the description of the movie

    * movie_genre - This field will store the genre of the movie

    * movie_raiting - This field will store the rating of the movie

    * movie_date_release - This field will store the release date of the movie

    * movie_age_limit - This field will store the age limit for the movie

    * path_to_the_image - This field will store the path to the photo to the movie
    """

    movie_title = models.CharField(
        max_length=30, 
        verbose_name="Название")

    movie_description = models.TextField(
        verbose_name="Описание")

    movie_genre = models.ForeignKey(
        'Model_for_storing_genres', 
        on_delete = models.PROTECT, 
        verbose_name="Жанр")

    movie_raiting = models.CharField(
        max_length=5, 
        verbose_name="Рейтинг")

    movie_date_release = models.CharField(
        max_length=20, 
        verbose_name="Дата выхода")

    movie_age_limit = models.CharField(
        max_length=10, 
        verbose_name="Возрастное ограничение")

    path_to_the_image = models.ImageField(
        upload_to='img/', 
        verbose_name="file")

    def __str__(self) -> str:
        """
        When accessing the class, returns the name of the Movie
        """
        return self.movie_title
        
    class Meta:
        """
        How it will be displayed in the django admin panel
        """
        verbose_name = "Фильм на страничке с фильмами"
        verbose_name_plural = "Фильмы на страничке с фильмами"

class Model_for_storing_series(models.Model):
    """Creates a model for storing serial data

    * serial_title - This field will store the name of the serial
    
    * serial_description - This field will store the description of the serial

    * serial_genre - This field will store the genre of the serial

    * serial_raiting - This field will store the rating of the serial

    * serial_date_release - This field will store the release date of the serial

    * serial_age_limit - This field will store the age limit for the serial

    * path_to_the_image - This field will store the path to the photo to the serial
    """
    serial_title = models.CharField(
        max_length=30, 
        verbose_name="Название")
    
    serial_description = models.TextField(
        verbose_name="Описание")

    serial_genre = models.ForeignKey(
        'Model_for_storing_genres', 
        on_delete = models.PROTECT, 
        verbose_name="Жанр")

    serial_raiting = models.CharField(
        max_length=5, 
        verbose_name="Рейтинг")

    serial_date_release = models.CharField(
        max_length=20, 
        verbose_name="Дата выхода")

    serial_age_limit = models.CharField(
        max_length=10, 
        verbose_name="Возрастное ограничение")

    path_to_the_image = models.ImageField(
        upload_to='img/', 
        verbose_name="file")

    def __str__(self) -> str:
        """
        When accessing the class, returns the name of the serial
        """
        return self.serial_title

    class Meta:
        """
        How it will be displayed in the django admin panel
        """
        verbose_name = "Сериал"
        verbose_name_plural = "Сериалы"

class Model_for_storing_genres(models.Model):
    """A model for storing genres
    
    * genre_name - The field stores the name of the genre

    """
    genre_name = models.CharField(
        max_length=50, 
        verbose_name="Жанр")

    def __str__(self):
        """
        When accessing the class, returns the name of the genre
        """
        return self.genre_name

    class Meta:
        """
        How it will be displayed in the django admin panel
        """
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"