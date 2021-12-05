const loginButtons = document.querySelectorAll(".js-button-login");
const modal = document.querySelector(".js-modal");
const closeButton = document.querySelector(".js-modal-close");
function showModalLogIn() {
	modal.classList.add("open");
}
function hideModalLogIn() {
	modal.classList.remove("open");
}

for (loginButton of loginButtons) {
	loginButton.addEventListener("click", showModalLogIn);
	closeButton.addEventListener("click", hideModalLogIn);
}

var header = document.getElementById("header");
var menuMobileIpad = document.getElementById("js-nav");
var buttonMenu = document.getElementById("js-menu-mobile-ipad");

// logup
const logupButtons = document.querySelectorAll(".js-button-logup");
const modal_up = document.querySelector(".js-modal_logup");
const closeButton_up = document.querySelector(".js-modal-close-up");
function showModalLogUp() {
	modal_up.classList.add("open");
}
function hideModalLogUp() {
	modal_up.classList.remove("open");
}
for (logupButton of logupButtons) {
	logupButton.addEventListener("click", showModalLogUp);
	closeButton_up.addEventListener("click", hideModalLogUp);
}
