from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import NewDepartmentForm
from .models import Department


@login_required
def departments(request):
    """
    This function get a list of departments from the database.
    """

    context = {'current_page': 'departments'}
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

    if request.method != 'POST':
        form = NewDepartmentForm()

    form = NewDepartmentForm(request.POST)

    if form.is_valid():
        name = form.cleaned_data["name"]
        description = form.cleaned_data["description"]

        if Department.objects.filter(name=name).exists():
            messages.error(request, "Department's name is already exists")
            return redirect('create-department')

        department = Department(name=name, description=description)
        department.save()

        messages.success(request, "Create department successfully")
        return redirect('departments')

    else:
        form = NewDepartmentForm()

    return render(request, 'new.html', {'form': form})
