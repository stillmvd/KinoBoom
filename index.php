<!DOCTYPE html>
<html lang = 'en' id = 'switch'>
<head>
    <meta charset = 'UTF-8'>
    <title>KinoBoom</title>
    <link rel = 'stylesheet' href = 'css/style.css'>
    <script src = 'js/main.js'></script>
</head>
<header id = 'header'>
    <div class = 'innerHeader container'>
        <div class = 'logoSpace'>
            <a href = 'index.php'>
                <img src = 'img/logo1.svg' alt = 'logo' id = 'logo'>
            </a>
        </div>
        <div class = 'navSpace'>
            <a href = '#'>
                Фильмы
            </a>
            <a href = '#'>
                Сериалы
            </a>
            <a href = '#'>
                Подписка
            </a>
            <img src = 'img/search.svg' alt = 'search' class = 'searchLoop' id = 'searchLoop' disabled>
            <p>Поиск</p>
        </div>
        <div class = 'avatarSpace'>
            <img onclick = 'modalOpen()' id = 'avatar' data-modal = 'modalOpen' src = 'img/user.svg' alt = 'user'>
        </div>
    </div>
    <div class = 'fullscreen'>
        <button id = 'fullscreen' onclick = 'fullscreen()'>

        </button>
    </div>
    <div class = 'flipContainer'>
        <div class = 'flipper'>
            <div class = 'modalWindLogin' id = 'modalWindLogin' data-modal = 'modalOpen'>
                <img src = 'img/cross.svg' alt = 'close' onclick = 'modalClose()' id = 'cross'>
                <p class = 'regTitle'>Войти</p>
                <form action = '' class = 'logForm'>
                    <input type = 'text' placeholder = 'Логин' name = 'userLog'>
                    <input type = 'text' placeholder = 'Пароль' name = 'userPass'>
                    <input type = 'submit' value = 'войти'>
                </form>
                <p class = 'question'>Зарегистрироваться</p>
            </div>
            <div class = 'modalWindReg' id = 'modalWindReg' data-modal = 'modalOpen'>
                <img src = 'img/cross.svg' alt = 'close' onclick = 'modalClose()' id = 'cross'>
                <p class = 'regTitle'>Войти</p>
                <form action = '' class = 'logForm'>
                    <input type = 'text' placeholder = 'Логин' name = 'userLog'>
                    <input type = 'text' placeholder = 'Пароль' name = 'userPass'>
                    <input type = 'submit' value = 'зарегистрироваться'>
                </form>
            </div>
        </div>
    </div>
</header>
<div class = 'overlay' id = 'overlay'>
            
</div>
<body>
    <div class = 'bodyContent container'>
        <div class = 'leftPart'>
            <div class = 'categories'>
                <a href = ''>Аниме</a>
                <a href = ''>Боевик</a>
                <a href = ''>Вестерн</a>
                <a href = ''>Детектив</a>
                <a href = ''>Детский</a>
                <a href = ''>Документальный</a>
                <a href = ''>Драма</a>
                <a href = ''>Комедия</a>
                <a href = ''>Мультфильм</a>
                <a href = ''>Мюзикл</a>
                <a href = ''>Приключения</a>
                <a href = ''>Семейный</a>
                <a href = ''>Спорт</a>
                <a href = ''>Триллер</a>
                <a href = ''>Ужасы</a>
                <a href = ''>Фэнтези</a>
            </div>
        </div>
        <div class = 'rightPart'>
            <h3 class = 'partTitle'>
                Новинки
            </h3>
            <div class = 'films'>
                <div class = 'preview hover' onmouseover = 'showInfo()' onmouseout = 'hideInfo()'>
                    <div class = 'filmInfo' id = 'filmInfo'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Warcraft
                        </h2>
                        <p class = 'filmDate'>
                            10 июня 2016 год
                        </p>
                    </div>
                </div>
                <div class = 'preview1 hover' onmouseover = 'showInfo1()' onmouseout = 'hideInfo1()'>
                    <div class = 'filmInfo1' id = 'filmInfo1'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Ангелы и демоны
                        </h2>
                        <p class = 'filmDate'>
                            13 мая 2009 год
                        </p>
                    </div>
                </div>
                <div class = 'preview2 hover' onmouseover = 'showInfo2()' onmouseout = 'hideInfo2()'>
                    <div class = 'filmInfo2' id = 'filmInfo2'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Пепел
                        </h2>
                        <p class = 'filmDate'>
                            27 октября 2013 год
                        </p>
                    </div>
                </div>
                <div class = 'preview3 hover' onmouseover = 'showInfo3()' onmouseout = 'hideInfo3()'>
                    <div class = 'filmInfo3' id = 'filmInfo3'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Zoмбилэнд
                        </h2>
                        <p class = 'filmDate'>
                            2 октября 2009 год
                        </p>
                    </div>
                </div>
                <div class = 'preview4 hover' onmouseover = 'showInfo4()' onmouseout = 'hideInfo4()'>
                    <div class = 'filmInfo4' id = 'filmInfo4'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Arrival
                        </h2>
                        <p class = 'filmDate'>
                            1 сентября 2016 год
                        </p>
                    </div>
                </div>
                <div class = 'preview5 hover' onmouseover = 'showInfo5()' onmouseout = 'hideInfo5()'>
                    <div class = 'filmInfo5' id = 'filmInfo5'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Glass
                        </h2>
                        <p class = 'filmDate'>
                            18 января 2019 год
                        </p>
                    </div>
                </div>
                <div class = 'preview6 hover' onmouseover = 'showInfo6()' onmouseout = 'hideInfo6()'>
                    <div class = 'filmInfo6' id = 'filmInfo6'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Доктор стрэндж
                        </h2>
                        <p class = 'filmDate'>
                            25 октября 2016 год
                        </p>
                    </div>
                </div>
                <div class = 'preview7 hover' onmouseover = 'showInfo7()' onmouseout = 'hideInfo7()'>
                    <div class = 'filmInfo7' id = 'filmInfo7'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Сталинград
                        </h2>
                        <p class = 'filmDate'>
                            10 октября 2013 год
                        </p>
                    </div>
                </div>
            </div>
            <div class = 'showMore'>
                <a href = '#'>
                    показать больше
                </a>
            </div>
            <h3 class = 'partTitle'>
                Популярное
            </h3>
            <div class = 'films'>
                <div class = 'preview8 hover' onmouseover = 'showInfo10()' onmouseout = 'hideInfo10()'>
                    <div class = 'filmInfo10' id = 'filmInfo10'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Мастер
                        </h2>
                        <p class = 'filmDate'>
                            14 февраля 2013 год
                        </p>
                    </div>
                </div>
                <div class = 'preview9 hover' onmouseover = 'showInfo11()' onmouseout = 'hideInfo11()'>
                    <div class = 'filmInfo11' id = 'filmInfo11'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Астрал
                        </h2>
                        <p class = 'filmDate'>
                            1 апреля 2011 год
                        </p>
                    </div>
                </div>
                <div class = 'preview10 hover' onmouseover = 'showInfo12()' onmouseout = 'hideInfo12()'>
                    <div class = 'filmInfo12' id = 'filmInfo12'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Матрица
                        </h2>
                        <p class = 'filmDate'>
                            31 марта 1999 год
                        </p>
                    </div>
                </div>
                <div class = 'preview11 hover' onmouseover = 'showInfo13()' onmouseout = 'hideInfo13()'>
                    <div class = 'filmInfo13' id = 'filmInfo13'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Evangeline
                        </h2>
                        <p class = 'filmDate'>
                            28 сентября 2016 год
                        </p>
                    </div>
                </div>
                <div class = 'preview12 hover' onmouseover = 'showInfo14()' onmouseout = 'hideInfo14()'>
                    <div class = 'filmInfo14' id = 'filmInfo14'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Still Born
                        </h2>
                        <p class = 'filmDate'>
                            29 апреля 2017 год
                        </p>
                    </div>
                </div>
                <div class = 'preview13 hover' onmouseover = 'showInfo15()' onmouseout = 'hideInfo15()'>
                    <div class = 'filmInfo15' id = 'filmInfo15'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Boogieman
                        </h2>
                        <p class = 'filmDate'>
                            24 марта 2005 год
                        </p>
                    </div>
                </div>
                <div class = 'preview14 hover' onmouseover = 'showInfo16()' onmouseout = 'hideInfo16()'>
                    <div class = 'filmInfo16' id = 'filmInfo16'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            Астрал 4
                        </h2>
                        <p class = 'filmDate'>
                            18 января 2018 год
                        </p>
                    </div>
                </div>
                <div class = 'preview15 hover' onmouseover = 'showInfo17()' onmouseout = 'hideInfo17()'>
                    <div class = 'filmInfo17' id = 'filmInfo17'>
                        <div class = 'darkMode'>
                            
                        </div>
                        <h2 class = 'filmTitle'>
                            The Scarehouse
                        </h2>
                        <p class = 'filmDate'>
                            13 сентября 2014 год
                        </p>
                    </div>
                </div>
            </div>
            <div class = 'showMore'>
                <a href = '#'>
                    показать больше
                </a>
            </div>
        </div>
    </div>
</body>
<footer>
    
</footer>
</html>