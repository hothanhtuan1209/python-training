function validateForm() {
  console.log("validateForm");
  var name = document.getElementById("inputName").value;
  var description = document.getElementById("inputDescription").value;
  if (name.trim() === "") {
    // set warning display to block
    document.getElementById("create-warning").style.display = "block";
      // don't submit form
      // alert("Name field is required");
    return false;
  }

  if (description.trim() === "") {
      // alert("Description field is required");
      return false;
    }
    return true;
}
