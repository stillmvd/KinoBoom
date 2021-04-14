let changeScreen = document.getElementById('switch');
let expandButton = document.getElementById('fullscreen');


function fullscreen() {
    if (changeScreen.requestFullscreen) changeScreen.requestFullscreen();
}

function changeIcon(event) {
    expandButton.style.backgroundImage = 'url(/img/outscreen.svg)';
}