var btnAbrirPopup2 = document.getElementById("btn-abrir-popup-2"),
  overlay2 = document.getElementById("overlay-2"),
  popup2 = document.getElementById("popup-2"),
  btnCerrarPopup2 = document.getElementById("btn-cerrar-popup-2");

btnAbrirPopup2.addEventListener("click", function () {
  overlay2.classList.add("active");
  popup2.classList.add("active");
});

btnCerrarPopup2.addEventListener("click", function (e) {
  e.preventDefault();
  overlay2.classList.remove("active");
  popup2.classList.remove("active");
});
