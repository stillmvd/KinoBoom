from django.http import request
from django.shortcuts import get_object_or_404, render, redirect
from django.utils.regex_helper import NonCapture
from .models import Model_for_storing_movies_from_the_main_page, \
                    Model_for_storing_movies_from_the_film_page, \
                    Model_for_storing_series, Model_for_storing_genres
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login

"""
A global variable that stores data whether the user is registered
"""
logged = False

"""
Further functions are secondary and are used to work 
with data and pass it to functions for output
"""

"""
These functions are used for user registration and login, logout

* First we get the data from the registration and login fields

* Secondly we expect that the user will want to register or log in

* Third we register and log in the user

* And in the end if the user wants to logout out then we logout him out

"""

def getting_data_from_post_fields_register(request):
    
    """The function gets results from post fields

    * username - Waits for a get request from a field named UserLog
    
    * usermail - Waits for a get request from a field named userMail

    * password - Waits for a get request from a field named userPassы

    Then there is a check for filling in the fields,
    and if they are filled in then the user is registered
    """
    global logged

    username = request.POST.get('userLog')
    usermail = request.POST.get('userMail')
    password = request.POST.get('userPass')
    
    return username, usermail, password

def getting_data_from_post_fields_login(request):
    """The function gets results from post fields
    
    * username - username of the user

    * password - password of the user

    """
    global logged

    username = request.POST.get('userLog')
    password = request.POST.get('userPass')

    return username, password

def waiting_for_registration_or_login(request):
    """The function is waiting for registration from the user
    
    * login_in_site - Takes data from the fields and logs in the user

    * register_in_site -Takes data from the fields and register in the user

    """
    login_in_site(
        request,
        getting_data_from_post_fields_login(request)[0],
        getting_data_from_post_fields_login(request)[1]
    )

    register_in_site(
        request,
        getting_data_from_post_fields_register(request)[0],
        getting_data_from_post_fields_register(request)[1],
        getting_data_from_post_fields_register(request)[2]
    )

def login_in_site(request,username,password):
    """
    The function logs the user on the site
    """
    global logged

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        if user.is_authenticated:
            logged = True

            return redirect('main/index.html')

def register_in_site(request,username,usermail,password):
    """
    The function register the user on the site
    """
    global logged

    if (username != None) and (usermail != None) and (password != None):

        try:
            user = User.objects.create_user(
                                    username=username, 
                                    email=usermail, 
                                    password=password
                                )

            user.save()
            user = authenticate(request, 
                        username=username, 
                        password=password
                    )

            if user is not None:
                login(request, user)

                if user.is_authenticated:
                    logged = True

                return redirect('main/index.html')

        except IntegrityError:
            pass

def logout(request):
    """
        Дописать!!!
    """
    global logged

    if request.method == 'GET':

        logged = False



"""
Further functions are needed to divide the content into specific subgroups
"""



def getting_movies_by_genre(request,genre_need):
    """Function for getting movies by genre
    
    * general_group_of_films - The first group is used to collect 
    movies from all pages by genre

    * first_subgroup_of_films - The second group is used to combine 
    the films of the subgroup by site

    For example there were 3 movies from the site with movies it 
    combines them into a subgroup and so on each page

    * final_group_of_films_by_genre -the final subgroup combines 
    all the subgroups of the second category for further output

    if there are no movies by genre it outputs not found
    """
    general_group_of_films = []
    subgroup_of_films = []
    final_group_of_films_by_genre = []

    general_group_of_films.append(Model_for_storing_movies_from_the_main_page.objects.filter(movie_genre = genre_need[0].id))
    general_group_of_films.append(Model_for_storing_movies_from_the_film_page.objects.filter(movie_genre = genre_need[0].id))
    general_group_of_films.append(Model_for_storing_series.objects.filter(movie_genre = genre_need[0].id))

    for film_id in range(0,len(general_group_of_films)):
        if len(general_group_of_films[film_id]) != 0:
            subgroup_of_films.append(general_group_of_films[film_id])

    try:
        for films_group in subgroup_of_films:
            final_group_of_films_by_genre += films_group

        return final_group_of_films_by_genre

    except IndexError:

            return render(
                        request=request, 
                        template_name='main/notfound.html'
                    )

def splits_serials_into_subclasses(serials_to_break_up):
    """The function separates serials from the database
    
    * subgroup_of_serials_Netflix - A subgroup containing series from Netflix

    * subgroup_of_serials_recommend - A subgroup containing recommended series
    
    """

    subgroup_of_serials_Netflix = []
    subgroup_of_serials_recommend = []

    try:

        for subgroup_of_serials_Netflix_item in range(0,8):
            subgroup_of_serials_Netflix.append(serials_to_break_up[subgroup_of_serials_Netflix_item])
        for subgroup_of_serials_recommend_item in range(8,17):
            subgroup_of_serials_recommend.append(serials_to_break_up[subgroup_of_serials_recommend_item])

    except IndexError:
        pass

    return subgroup_of_serials_Netflix, \
           subgroup_of_serials_recommend

def splits_movies_into_subclasses(movies_to_break_up):
    """The function separates movies from the database
    
    * subgroup_of_serials_Netflix - A subgroup containing new_movies

    * subgroup_of_serials_recommend - A subgroup containing popular_movies
    
    """

    subgroup_of_new_movies = []
    subgroup_of_popular_movies = []

    try:

        for subgroup_of_new_movies_item in range(0,8):
            subgroup_of_new_movies.append(movies_to_break_up[subgroup_of_new_movies_item])
        for subgroup_of_popular_movies_item in range(8,17):
            subgroup_of_popular_movies.append(movies_to_break_up[subgroup_of_popular_movies_item])

    except IndexError:
        pass

    return subgroup_of_new_movies, \
           subgroup_of_popular_movies



"""
Further functions are needed to work with users
"""


def search(request):
    """the function performs a site search
    
    * userSearch - Receives a request from the user

    * film_userSearch_in_main_page - Searches for a movie on demand on the site main_pag

    * film_userSearch_in_film_page - Searches for a movie on demand on the site film_page

    * serials_userSearch_in_serials_page - Searches for a serials on demand on the site serials_page

    Next, the found movie displays on the movie page ( filmPage )
    """

    if request.method == 'GET':

        if request.GET.get('userSearch'):

            userSearch = request.GET.get('userSearch').capitalize()
            
            film_userSearch_in_main_page = Model_for_storing_movies_from_the_main_page.objects.filter(
                    movie_title = userSearch)
            film_userSearch_in_film_page = Model_for_storing_movies_from_the_film_page.objects.filter(
                    movie_title = userSearch)
            serials_userSearch_in_serials_page = Model_for_storing_series.objects.filter(
                    movie_title = userSearch)

            try:

                if len(film_userSearch_in_main_page) != 0:

                    film = film_userSearch_in_main_page[0]

                    context = {
                        "film" : film
                    }

                    return render(
                                request=request, 
                                template_name='main/filmPage.html', 
                                context=context
                            )

                elif len(film_userSearch_in_film_page) != 0:

                    film = film_userSearch_in_film_page[0]
                        
                    context = {
                        "film" : film
                    }

                    return render(
                                request=request, 
                                template_name='main/filmPage.html', 
                                context=context
                            )

                elif len(serials_userSearch_in_serials_page) != 0:

                    film = serials_userSearch_in_serials_page[0]

                    context = {
                        "film" : film   
                    }

                    return render(
                                request=request, 
                                template_name='main/filmPage.html', 
                                context=context
                            )    

            except ValueError:

                return render(
                    request=request, 
                    template_name='main/notfound.html')

            except IndexError:

                return render(
                    request=request, 
                    template_name='main/notfound.html')

            return render(
                        request=request, 
                        template_name='main/notfound.html'
            )
            

def change_user_data(request):
    pass




"""
Further functions are used to display the received data to the site
"""



def podpiska(request):
    """
    Displays the subscription site
    """
    
    waiting_for_registration_or_login(request)

    context = {
        "logged" : logged
    }

    return render(
            request=request, 
            template_name='main/podpiska.html',
            context=context
            )

def cabinet(request):
    """
    Displays the cabinet site
    """

    logout(request)

    context = {
        "user" : request.user
    }
    
    return render(
                request=request, 
                template_name='main/cabinet.html',
                context=context
            )

def notfound(request):
    """
    Displays the site 404
    """

    return render(
                request=request, 
                template_name='main/notfound.html'
            )

def index(request):
    """
    Displays the site main site
    """

    search(request)
    waiting_for_registration_or_login(request)

    genres = Model_for_storing_genres.objects.all()
    film = Model_for_storing_movies_from_the_main_page.objects.all()

    context = {
        "genre" : genres,
        "films_new" : splits_movies_into_subclasses(film)[0],
        "films_popular" : splits_movies_into_subclasses(film)[1],
        "logged" : logged 
    }

    return render(
                request=request, 
                template_name='main/index.html', 
                context=context
            )
        
def films(request):
    """
    Displays a website with movies
    """

    search(request)
    waiting_for_registration_or_login(request)
    

    genres = Model_for_storing_genres.objects.all()
    film = Model_for_storing_movies_from_the_film_page.objects.all()

    context = {
        "genre" : genres,
        "films_new" : splits_movies_into_subclasses(film)[0],
        "films_popular" : splits_movies_into_subclasses(film)[1],
        "logged" : logged 
    }

    return render(
                request=request, 
                template_name='main/films.html', 
                context=context
            )

def serials(request):
    """
    Displays a website with series
    """

    search(request)
    waiting_for_registration_or_login(request)

    serials = Model_for_storing_series.objects.all()
    genres = Model_for_storing_genres.objects.all()

    context = {
        'genre' : genres,
        'serials' : serials,
        'serials_Netflix' : splits_serials_into_subclasses(serials)[0],
        'serials_recommend' : splits_serials_into_subclasses(serials)[1],
        "logged" : logged 
    }

    return render(
                request=request, 
                template_name='main/serials.html',
                context=context
            )

def movies_by_genre(request, genre_id):
    """
    function for displaying movies by genre

    if there are no movies by genre it outputs not found(  if movies_by_genre == []  )
    """

    genre_need = Model_for_storing_genres.objects.filter(id=genre_id)
    genres_all = Model_for_storing_genres.objects.all()
    movies_by_genre = getting_movies_by_genre(request,genre_need)
    
    if movies_by_genre == []:

        return render(
                    request=request, 
                    template_name='main/notfound.html'
                )

    context = {
        "genres1" : genre_need[0],
        "genres" : genres_all,
        "films" : movies_by_genre
    }
    
    return render(
                request=request, 
                template_name='main/genrePage.html', 
                context=context
            )

def film(request, film_id, movie_title):
    """Function for displaying a movie when you click 

    Check the Id and title if there is a match outpu
    """

    film_id_main_page = Model_for_storing_movies_from_the_main_page.objects.filter(
            id = film_id)
    film_id_film_page = Model_for_storing_movies_from_the_film_page.objects.filter(
            id = film_id)
    serials_id_serials_page = Model_for_storing_series.objects.filter(
            id = film_id)

    film_title_main_page = Model_for_storing_movies_from_the_main_page.objects.filter(
            movie_title = movie_title)
    film_title_film_page = Model_for_storing_movies_from_the_film_page.objects.filter(
            movie_title = movie_title)   
    serials_title_serials_page = Model_for_storing_series.objects.filter(
            movie_title = movie_title)

    if film_id_main_page and film_title_main_page:

        film = film_title_main_page[0]

        context = {
            "film" : film
        }

        return render(
                    request=request, 
                    template_name='main/filmPage.html', 
                    context=context
                )

    elif film_id_film_page and film_title_film_page:

        film = film_title_film_page[0]
            
        context = {
            "film" : film
        }

        return render(
                    request=request, 
                    template_name='main/filmPage.html', 
                    context=context
                )

    elif serials_id_serials_page and serials_title_serials_page:

        film = serials_title_serials_page[0]

        context = {
            "film" : film   
        }

        return render(
                    request=request, 
                    template_name='main/filmPage.html', 
                    context=context
                )