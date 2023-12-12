from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Department
from django.http import JsonResponse


@login_required
def departments(request):
    """
    This function get a list of departments from the database.
    """

    context = {"current_page": "departments"}
    departments = Department.objects.all().order_by("-id")[:10]
    return render(
        request, "list.html", {"departments": departments, "context": context}
    )


@login_required
def create_department(request):
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
