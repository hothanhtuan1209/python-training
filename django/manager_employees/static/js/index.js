document.addEventListener("DOMContentLoaded", function () {
  console.log('Tuan')
  var myForm = document.getElementById("myForm");
  var editForm = document.getElementById("myFormEdit");

  if (myForm) {
    myForm.addEventListener("submit", function (event) {
      event.preventDefault();
      var isValid = validateForm(myForm);
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
  
  }
  
  function validateForm(form) {
    var isValid = true;
    var name = form.querySelector("#inputName").value;
    var description = form.querySelector("#inputDescription").value;

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

  // 
  console.log("form", editForm)
  if (editForm) {
    editForm.addEventListener("submit", function (event) {
      console.log("form")
      event.preventDefault();
      saveDepartmentChanges();
    });
  }



  function saveDepartmentChanges() {
    var isValid = validateForm(myFormEdit);
    if (!isValid) {
      return;
    }

    var formData = new FormData(myFormEdit);
    var xhr = new XMLHttpRequest();
    var url = myFormEdit.getAttribute("action");
    console.log('sssss',  new FormData(myFormEdit))
    xhr.open(
      "PATCH",
      `${url}`,
      true
    );

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

  function deleteDepartment(departmentId) {
    fetch(`/departments/${departmentId}/`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCookie('csrftoken'),
      },
    })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          alert('Department deleted successfully');
          location.reload();
        } else {
          alert('Error: ' + data.error_message);
        }
      })
      .catch(error => console.error('Error:', error));
  }
  // function setDeleteDepartmentId(departmentId) {
  //   document.getElementById('deleteDepartmentId').value = departmentId;
  // }
  
  function myConfirmDelete() {
    console.log('Confirming delete...');
    var departmentId = document.getElementById('deleteDepartmentId').value;
    deleteDepartment(departmentId);
  }
});
