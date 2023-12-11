// script.js
document.addEventListener("DOMContentLoaded", function () {
  var addNewButton = document.querySelector(".add-button");
  var formNew = document.querySelector(".form-new");
  var cancelButton = document.querySelector(".cancel");

  addNewButton.addEventListener("click", (e) => {
    e.preventDefault();
    formNew.style.display = "flex";
  });

  cancelButton.addEventListener("click", (e) => {
    e.preventDefault();
    formNew.style.display = "none";
  });
});
