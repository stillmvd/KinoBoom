from django.shortcuts import get_object_or_404, render, redirect
from django.utils.regex_helper import NonCapture
from .models import Model_for_storing_movies_from_the_main_page, \
                    Model_for_storing_movies_from_the_film_page, \
                    Model_for_storing_series, Model_for_storing_genres
from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login

errors_user = False
logged = False
confirm_password = True
user = ''

def is_number(str):
    """
    Checking for a number in a string
    """
    try:

        float(str)
        return True

    except ValueError:

        return False
def logout(request):
    global logged
    if request.method == 'GET':
        logged = False

def search(request):
    if request.method == 'GET':
        if request.GET.get('userSearch'):
            userSearch = request.GET.get('userSearch').capitalize()
            print(userSearch)
            try:
                if len(Model_for_storing_movies_from_the_main_page.objects.filter(
                    movie_title = userSearch)) != 0:
                    print(1)
                    film = Model_for_storing_movies_from_the_main_page.objects.filter(
                        movie_title = userSearch)[0]

                    context = {
                        "film" : film
                    }

                    return render(
                        request=request, 
                        template_name='main/filmPage.html', 
                        context=context)

                elif len(Model_for_storing_movies_from_the_film_page.objects.filter(
                    movie_title = userSearch)) != 0:
                    print(1)

                    film = Model_for_storing_movies_from_the_film_page.objects.filter(
                        movie_title = userSearch)[0]
                        
                    context = {
                        "film" : film
                    }

                    return render(
                        request=request, 
                        template_name='main/filmPage.html', 
                        context=context)

                elif len(Model_for_storing_series.objects.filter(
                    movie_title = userSearch)) != 0:

                    print(1)

                    film = Model_for_storing_series.objects.filter(
                        movie_title = userSearch)[0]

                    context = {
                        "film" : film   
                    }

                    return render(
                        request=request, 
                        template_name='main/filmPage.html', 
                        context=context)      

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
    global logged, errors_user
    """The function changes the user's data
    
    * user - 
    
    * changeName -

    * changeSecondName - 

    * changeMail - 

    * changePassword - 

    * confirmPassword -
    
    """

    logged = False

    user = getting_data_from_post_fields_login(request)
    changeName = request.GET.get('changeName')
    changeSecondName = request.GET.get('changeSecondName')
    changeMail = request.GET.get('changeMail')
    changePassword = request.GET.get('changePassword')
    confirmPassword = request.GET.get('changePassword2')

    if (changeName != None) and ((len(changeName)>10)\
        and (is_number(changeName)==False)):
        
        user.first_name = changeName
        user.save()

    elif (changeSecondName != None) and ((len(changeName)>10)\
        and (is_number(changeName)==False)):
        
        user.last_name = changeSecondName
        user.save()

    elif (changeMail != None) and ('@' in changeMail):
        
        user.email = changeMail
        user.save()

    elif changePassword != None:

        if changePassword == confirmPassword:

            if request.user.is_authenticated():

                username = user.username
                user = User.objects.get(username=username)
                user.set_password(changePassword)
                user.save()
    return user
def getting_data_from_post_fields_login(request):
    """The function gets results from post fields
    



    """
    global logged, errors_user
    username = request.POST.get('userLog')
    password = request.POST.get('userPass')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if user.is_authenticated:
            logged = True
            return redirect('main/index.html')

def getting_data_from_post_fields_register(request):
    
    """The function gets results from post fields

    * username - Waits for a get request from a field named UserLog
    
    * usermail - Waits for a get request from a field named userMail

    * password - Waits for a get request from a field named userPassы
    
    * errors_user - If the user is already registered = True, else = False

    Then there is a check for filling in the fields,
    and if they are filled in then the user is registered
    """
    global logged, errors_user
    username = request.POST.get('userLog')
    usermail = request.POST.get('userMail')
    password = request.POST.get('userPass')
    
    if username != None and usermail != None and password != None:
        
        try:
            user = User.objects.create_user(
                username=username, 
                email=usermail, 
                password=password)
            user.save()
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_authenticated:
                    logged = True
                return redirect('main/index.html')
        except IntegrityError:
            errors_user = True
    
def splits_serials_into_subclasses(serials_to_break_up):
    """The function separates serials from the database
    
    * subgroup_of_serials_Netflix - A subgroup containing series from Netflix

    * subgroup_of_serials_recommend - A subgroup containing recommended series
    
    """

    subgroup_of_serials_Netflix = []
    subgroup_of_serials_recommend = []

    try:
        for i in range(0,8):
            subgroup_of_serials_Netflix.append(serials_to_break_up[i])
        for y in range(8,17):
            subgroup_of_serials_recommend.append(serials_to_break_up[y])
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
        for i in range(0,8):
            subgroup_of_new_movies.append(movies_to_break_up[i])
        for y in range(8,17):
            subgroup_of_popular_movies.append(movies_to_break_up[y])
    except IndexError:
        pass

    return subgroup_of_new_movies, \
           subgroup_of_popular_movies

def podpiska(request):
    """
    Displays the subscription site
    """
    
    getting_data_from_post_fields_register(request)
    getting_data_from_post_fields_login(request)
    context = {
        "logged" : logged
    }
    return render(
        request=request, 
        template_name='main/podpiska.html',
        context=context)

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
        context=context)

def notfound(request):
    """
    Displays the site 404
    """

    return render(
        request=request, 
        template_name='main/notfound.html')

def index(request):
    """
    Displays the site main site
    """
    search(request)
    getting_data_from_post_fields_register(request)
    getting_data_from_post_fields_login(request)
    genres = Model_for_storing_genres.objects.all()
    film = Model_for_storing_movies_from_the_main_page.objects.all()
    context = {
        "genre" : genres,
        "films_new" : splits_movies_into_subclasses(film)[0],
        "films_popular" : splits_movies_into_subclasses(film)[1],
        "errors_user" : errors_user,
        "logged" : logged 
    }

    return render(
        request=request, 
        template_name='main/index.html', 
        context=context)
        
def films(request):
    """
    Displays a website with movies
    """

    search(request)
    getting_data_from_post_fields_register(request)
    getting_data_from_post_fields_login(request)
    
    genres = Model_for_storing_genres.objects.all()
    film= Model_for_storing_movies_from_the_film_page.objects.all()

    context = {
        "genre" : genres,
        "films_new" : splits_movies_into_subclasses(film)[0],
        "films_popular" : splits_movies_into_subclasses(film)[1],
        "errors_user" : errors_user,
        "logged" : logged 
    }

    return render(
        request=request, 
        template_name='main/films.html', 
        context=context)

def serials(request):
    """
    Displays a website with series
    """
    search(request)
    getting_data_from_post_fields_register(request)
    getting_data_from_post_fields_login(request)
    serials = Model_for_storing_series.objects.all()
    genres = Model_for_storing_genres.objects.all()

    context = {
        'genre' : genres,
        'serials' : serials,
        'serials_Netflix' : splits_serials_into_subclasses(serials)[0],
        'serials_recommend' : splits_serials_into_subclasses(serials)[1],
        "errors_user" : errors_user,
        "logged" : logged 
    }

    return render(
        request=request, 
        template_name='main/serials.html',
        context=context)
