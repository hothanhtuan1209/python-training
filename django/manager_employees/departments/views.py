from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Department


@login_required
def departments(request):
    """
    This function get a list of departments from the database.
    """

    context = {'current_page': 'departments'}
    departments = Department.objects.all()
    return render(request, 'list.html', {
        'departments': departments, 'context': context
    })


@login_required
def create_department(request):
    """
    View function for creating a new department.

    If the request method is GET, it renders the form to create a new
    department. If the request method is POST, it processes the
    form submission.
    """

    error_message = None

    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        if Department.objects.filter(name=name).exists():
            error_message = "Department's name is already exists"
        else:
            department = Department(name=name, description=description)
            try:
                department.save()
                messages.success(request, "Create department successfully")
                return redirect('departments')
            except Exception as e:
                error_message = f"Error saving department: {e}"

    return render(request, 'list.html', {'error_message': error_message})