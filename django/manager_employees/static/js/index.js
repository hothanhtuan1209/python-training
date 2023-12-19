document.addEventListener("DOMContentLoaded", function () {
  var myForm = document.getElementById("myForm");
  var editForm = document.getElementById("myFormEdit"); // Thêm dòng này

  myForm.addEventListener("submit", function (event) {
    event.preventDefault();
    var isValid = validateForm();
    if (isValid) {
      var formData = new FormData(myForm);
      var xhr = new XMLHttpRequest();
      xhr.open("POST", myForm.action, true);
      xhr.onload = function () {
        if (xhr.status === 200) {
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

  editForm.addEventListener("submit", function (event) {
    event.preventDefault();
    saveDepartmentChanges();
  });

  function saveDepartmentChanges() {
    var formData = new FormData(editForm);
    var xhr = new XMLHttpRequest();
    xhr.open("PATCH", `/departments/${document.getElementById("departmentID").value}/`, true);

    xhr.onload = function () {
      if (xhr.status === 200) {
        var response = JSON.parse(xhr.responseText);
        handleResponse(response);
      } else {
        alert("Error saving changes.");
      }
    };

    xhr.onerror = function () {
      console.error("Request failed.");
    };

    xhr.send(formData);
  }

  function handleResponse(response) {
    if (response.success) {
      alert("Changes saved successfully");
      location.reload();
    } else {
      alert("Error: " + response.error_message);
    }
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
      document.getElementById("departmentID").value = response.id;
      document.getElementById("departmentTime").value = response.created_at;
      document.getElementById("editNameDepartment").value = response.name;
      document.getElementById("editDescription").value = response.description;
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
