document.addEventListener("DOMContentLoaded", function () {
  var myForm = document.getElementById("myForm");
  myForm.addEventListener("submit", function (event) {
    event.preventDefault();
    var isValid = validateForm();
    if (isValid) {
      // Get the form data
      var formData = new FormData(myForm);
      // send the form data by AJAX
      var xhr = new XMLHttpRequest();
      xhr.open("POST", myForm.action, true);
      // Handle the server response
      xhr.onload = function () {
        if (xhr.status === 200) {
          // Parse the JSON response
          var response = JSON.parse(xhr.responseText);

          if (response.success) {
            alert("Create department successfully");
            location.reload();
          } else {
            alert("Error: " + response.error_message);
          }
        } else {
          var response = JSON.parse(xhr.responseText);
          alert("Error: " + response.error_message);
        }
      };
      // Handle error durung AJAX request
      xhr.onerror = function () {
        console.error("Request failed.");
      };
      xhr.send(formData); 
    }
  });

  function validateForm() {
    var isValid = true;
    var name = document.getElementById("inputName").value;
    var description = document.getElementById("inputDescription").value;
    if (name.trim() === "") {
      document.getElementById("error-message_name").innerText =
        "Name field is required";
      isValid = false;
    }
    if (description.trim() === "") {
      document.getElementById("error-message_description").innerText =
        "Description field is required";
      isValid = false;
    }
    return isValid;
  }
});


function clearErrorMessageName() {
  const errorMessageElement =
    document.getElementById("error-message_name");
  errorMessageElement.innerText = "";
}


function clearErrorMessageDes() {
  const errorMessageElement = document.getElementById(
    "error-message_description"
  );
  errorMessageElement.innerText = "";
}


function showDepartmentDetails(departmentId) {
  var xhr = new XMLHttpRequest();
  xhr.open("GET", `/departments/${departmentId}`, true);

  xhr.onload = function () {
    if (xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);

      // Populate the form fields with the received data
      document.getElementById("departmentID").value = response.id;
      document.getElementById("departmentTime").value = response.created_at;
      document.getElementById("editNameDepartment").value = response.name;
      document.getElementById("editDescription").value = response.description;
      // Open the modal
      $("#myModalEdit").modal("show");
    } else {
      console.error("Failed to fetch department details.");
    }
  };

  xhr.onerror = function () {
    console.error("Request failed.");
  };

  xhr.send();
}
