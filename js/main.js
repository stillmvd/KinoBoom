let changeScreen = document.getElementById('switch');
let expandButton = document.getElementById('fullscreen');

function fullscreen() {
    if (changeScreen.requestFullscreen) changeScreen.requestFullscreen();
}

document.addEventListener('fullscreenchange', (event) => {
    if (document.fullscreenElement) {
        document.getElementById('fullscreen').style.opacity = '0%';
    } else {
        document.getElementById('fullscreen').style.opacity = '60%';
    }
});

function openSearch() {
    document.getElementById('bodyContent').style.marginTop = '64px';
    document.getElementById('searchSpace').style.top = '66px';
    document.getElementById('searchbar').style.opacity = '100%';
    document.getElementById('searchbar').classList.add('active');
}

function placeholder() {
    inputPlaceholder(document.getElementById('searchbar')).style.color = 'white';
}

function closeSearch() {
    document.getElementById('bodyContent').style.marginTop = '50px';
    document.getElementById('searchSpace').style.top = '-66px';
    document.getElementById('searchbar').style.opacity = '0%';
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
    document.getElementById('modalWindLogin').style.transform = 'translate(-50%, -50%)';
    document.getElementById('modalWindLogin').style.opacity = '100%';
    document.getElementById('overlay').style.opacity = '100%';
    document.getElementById('overlay').style.visibility = 'visible';
}

function modalClose() {
    document.getElementById('modalWindLogin').style.transform = 'translate(-50%, -250%)';
    document.getElementById('modalWindLogin').style.opacity = '0%';
    document.getElementById('overlay').style.opacity = '0%';
    document.getElementById('overlay').style.visibility = 'hidden';
}

document.addEventListener('keydown', function(event) {
    if (event.code == 'Escape') {
        modalClose();
    }
});

// useless

function showInfo() {   
    document.getElementById('filmInfo').style.opacity = '100%';
}

function hideInfo() {   
    document.getElementById('filmInfo').style.opacity = '0%';
}

function showInfo1() {   
    document.getElementById('filmInfo1').style.opacity = '100%';
}

function hideInfo1() {   
    document.getElementById('filmInfo1').style.opacity = '0%';
}

function showInfo2() {   
    document.getElementById('filmInfo2').style.opacity = '100%';
}

function hideInfo2() {   
    document.getElementById('filmInfo2').style.opacity = '0%';
}

function showInfo3() {   
    document.getElementById('filmInfo3').style.opacity = '100%';
}

function hideInfo3() {   
    document.getElementById('filmInfo3').style.opacity = '0%';
}

function showInfo4() {   
    document.getElementById('filmInfo4').style.opacity = '100%';
}

function hideInfo4() {   
    document.getElementById('filmInfo4').style.opacity = '0%';
}

function showInfo5() {   
    document.getElementById('filmInfo5').style.opacity = '100%';
}

function hideInfo5() {   
    document.getElementById('filmInfo5').style.opacity = '0%';
}

function showInfo6() {   
    document.getElementById('filmInfo6').style.opacity = '100%';
}

function hideInfo6() {   
    document.getElementById('filmInfo6').style.opacity = '0%';
}

function showInfo7() {   
    document.getElementById('filmInfo7').style.opacity = '100%';
}

function hideInfo7() {   
    document.getElementById('filmInfo7').style.opacity = '0%';
}

function showInfo8() {   
    document.getElementById('filmInfo8').style.opacity = '100%';
}

function hideInfo8() {   
    document.getElementById('filmInfo8').style.opacity = '0%';
}

function showInfo9() {   
    document.getElementById('filmInfo9').style.opacity = '100%';
}

function hideInfo9() {   
    document.getElementById('filmInfo9').style.opacity = '0%';
}

function showInfo10() {   
    document.getElementById('filmInfo10').style.opacity = '100%';
}

function hideInfo10() {   
    document.getElementById('filmInfo10').style.opacity = '0%';
}

function showInfo11() {   
    document.getElementById('filmInfo11').style.opacity = '100%';
}

function hideInfo11() {   
    document.getElementById('filmInfo11').style.opacity = '0%';
}

function showInfo12() {   
    document.getElementById('filmInfo12').style.opacity = '100%';
}

function hideInfo12() {   
    document.getElementById('filmInfo12').style.opacity = '0%';
}

function showInfo13() {   
    document.getElementById('filmInfo13').style.opacity = '100%';
}

function hideInfo13() {   
    document.getElementById('filmInfo13').style.opacity = '0%';
}

function showInfo14() {   
    document.getElementById('filmInfo14').style.opacity = '100%';
}

function hideInfo14() {   
    document.getElementById('filmInfo14').style.opacity = '0%';
}

function showInfo15() {   
    document.getElementById('filmInfo15').style.opacity = '100%';
}

function hideInfo15() {   
    document.getElementById('filmInfo15').style.opacity = '0%';
}

function showInfo16() {   
    document.getElementById('filmInfo16').style.opacity = '100%';
}

function hideInfo16() {   
    document.getElementById('filmInfo16').style.opacity = '0%';
}

function showInfo17() {   
    document.getElementById('filmInfo17').style.opacity = '100%';
}

function hideInfo17() {   
    document.getElementById('filmInfo17').style.opacity = '0%';
}