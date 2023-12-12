function createDepartment() {
  var form = document.getElementById('createDepartmentForm');
  var errorMessageContainer = document.getElementById('error-message');
  var nameErrorContainer = document.getElementById('name-error');
  var descriptionErrorContainer = document.getElementById('description-error');

  // Clear previous error messages
  errorMessageContainer.innerHTML = '';
  nameErrorContainer.innerHTML = '';
  descriptionErrorContainer.innerHTML = '';

  // Validate if required fields are not empty
  if (!form.elements['name'].value.trim()) {
    nameErrorContainer.innerHTML = '<p class="error-message">Name is required</p>';
    return;
  }

  if (!form.elements['description'].value.trim()) {
    descriptionErrorContainer.innerHTML = '<p class="error-message">Description is required</p>';
    return;
  }

  fetch(form.action, {
    method: 'POST',
    body: new FormData(form),
    headers: {
      'X-Requested-With': 'XMLHttpRequest',
      'X-CSRFToken': '{{ csrf_token }}'
    }
  })
  .then(response => response.json())
  .then(data => {
    if (data.error_message) {
      errorMessageContainer.innerHTML = `<p class="error-message">${data.error_message}</p>`;
    } else if (data.success) {
      // If the response indicates success, hide the form and do any other necessary actions
      document.getElementById('formNew').style.display = 'none';
    }
  });
}