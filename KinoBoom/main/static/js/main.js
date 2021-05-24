let changeScreen = document.getElementById('switch');
let expandButton = document.getElementById('fullscreen');

function fullscreen() {
    if (changeScreen.requestFullscreen) changeScreen.requestFullscreen();
}

document.addEventListener('fullscreenchange', (event) => {
    if (document.fullscreenElement) {
        document.getElementById('fullscreen').style.opacity = '0%';
        document.getElementById('nothing').style.paddingBottom = '31px';
        
    } else {
        document.getElementById('fullscreen').style.opacity = '60%';
        document.getElementById('nothing').style.paddingBottom = '0px';
    }
});

function openSearch() {
    document.getElementById('searching').style.display = 'block';
    document.getElementById('searchbar').style.opacity = '100%';
    document.getElementById('bodyContent').style.marginTop = '0px';
    document.getElementById('searchbar').classList.add('active');
}

function closeSearch() {
    document.getElementById('searching').style.display = 'none';
    document.getElementById('searchbar').style.opacity = '0%';
    document.getElementById('bodyContent').style.marginTop = '40px';
    document.getElementById('searchbar').classList.remove('active');
}

function checkSearch() {
    if (document.getElementById('searchbar').classList.contains('active')) {
        closeSearch();
    } else {
        openSearch();
    }
}

function modalOpen() {
    document.getElementById('modalWindLogin').style.opacity = '100%';
    document.getElementById('modalWindReg').style.opacity = '100%';
    document.getElementById('modalWindLogin').style.visibility = 'visible';
    document.getElementById('modalWindReg').style.visibility = 'visible';
    document.getElementById('overlay').style.opacity = '100%';
    document.getElementById('overlay').style.visibility = 'visible';
}

function modalClose() {
    document.getElementById('modalWindLogin').style.opacity = '0%';
    document.getElementById('modalWindReg').style.opacity = '0%';
    document.getElementById('modalWindLogin').style.visibility = 'hidden';
    document.getElementById('modalWindReg').style.visibility = 'hidden';
    document.getElementById('overlay').style.opacity = '0%';
    document.getElementById('overlay').style.visibility = 'hidden';
}

function modalChangeReg() {
    document.getElementById('modalWindLogin').style.transform = 'rotateY(-180deg)';
    document.getElementById('modalWindReg').style.transform = 'rotateY(180deg)';
    document.getElementById('modalWindReg').style.transform = 'translateZ(-2px)';
}

function modalChangeLog() {
    document.getElementById('modalWindReg').style.transform = 'rotateY(180deg)';
    document.getElementById('modalWindLogin').style.transform = 'rotateY(10deg)';
}

function aboutOpen() {
    document.getElementById('about').style.opacity = '100%';
    document.getElementById('about').style.visibility = 'visible';
    document.getElementById('overlay').style.opacity = '100%';
    document.getElementById('overlay').style.visibility = 'visible';
}

function aboutClose() {
    document.getElementById('about').style.opacity = '0%';
    document.getElementById('about').style.visibility = 'hidden';
    document.getElementById('overlay').style.opacity = '0%';
    document.getElementById('overlay').style.visibility = 'hidden';
}

document.addEventListener('keydown', function(event) {
    if (event.code == 'Escape') {
        modalClose();
        closeSearch();
    }
});

document.addEventListener('keydown', function(event) {
    if (event.code == 'Escape') {
        aboutClose();
    }
});

// Логин
function fixing() {
    document.getElementById('changeLogin').style.transform = 'translateY(0px)';
    document.getElementById('changeLogin').style.visibility = 'visible';
    document.getElementById('changeLogin').style.opacity = '1';
    document.getElementById('changeMail').style.transform = 'translateY(0px)';
    document.getElementById('changeMail').style.opacity = '0%';
    document.getElementById('changeMail').style.visibility = 'hidden';
    document.getElementById('changePassword').style.transform = 'translateY(0px)';
    document.getElementById('changePassword').style.opacity = '0%';
    document.getElementById('changePassword').style.visibility = 'hidden';
    document.getElementById('userName').style.visibility = 'hidden';
    document.getElementById('userEmail').style.visibility = 'hidden';
    document.getElementById('logout').style.visibility = 'hidden';
}

// Почта
function fixing2() {
    document.getElementById('changeMail').style.transform = 'translateY(0px)';
    document.getElementById('changeMail').style.visibility = 'visible';
    document.getElementById('changeMail').style.opacity = '1';
    document.getElementById('changeLogin').style.transform = 'translateY(0px)';
    document.getElementById('changeLogin').style.opacity = '0%';
    document.getElementById('changeLogin').style.visibility = 'hidden';
    document.getElementById('changePassword').style.transform = 'translateY(0px)';
    document.getElementById('changePassword').style.opacity = '0%';
    document.getElementById('changePassword').style.visibility = 'hidden';
    document.getElementById('userName').style.visibility = 'hidden';
    document.getElementById('userEmail').style.visibility = 'hidden';
    document.getElementById('logout').style.visibility = 'hidden';
}

// Пароль
function fixing3() {
    document.getElementById('changePassword').style.transform = 'translateY(0px)';
    document.getElementById('changePassword').style.visibility = 'visible';
    document.getElementById('changePassword').style.opacity = '1';
    document.getElementById('changeLogin').style.transform = 'translateY(0px)';
    document.getElementById('changeLogin').style.opacity = '0%';
    document.getElementById('changeLogin').style.visibility = 'hidden';
    document.getElementById('changeMail').style.transform = 'translateY(0px)';
    document.getElementById('changeMail').style.opacity = '0%';
    document.getElementById('changeMail').style.visibility = 'hidden';
    document.getElementById('userName').style.visibility = 'hidden';
    document.getElementById('userEmail').style.visibility = 'hidden';
    document.getElementById('logout').style.visibility = 'hidden';
}
