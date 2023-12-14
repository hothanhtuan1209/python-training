from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Department


@login_required
def departments(request):
    """
    This function get a list of departments from the database.
    """

    departments = Department.objects.all().order_by("-created_at")[:10]
    context = {"departments": departments, "current_page": "departments"}
    return render(request, "list.html", context)


@login_required
def create_department(request):
    """
    Handles the creation of a new department.

    Parameters:
        - request (HttpRequest): The HTTP request object.

    Returns:
        - JsonResponse: JSON response indicating the success or failure of the
        operation.
    """

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")

        if Department.objects.filter(name=name).exists():
            return JsonResponse(
                {"error_message": "Department's name is already exists"}, status=400
            )
        else:
            department = Department(name=name, description=description)
            try:
                department.save()
                messages.success(request, "Create department successfully")
                return JsonResponse({"success": True})
            except Exception as e:
                return JsonResponse(
                    {"error_message": f"Error saving department: {e}"}, status=500
                )

    return render(request, "list.html")
