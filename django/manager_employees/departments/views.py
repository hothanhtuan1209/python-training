from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from .models import Department
from employees.models import Employee


@login_required
@require_http_methods(["GET", "POST"])
def departments(request):
    """
    This function gets a list of departments from the database.
    """

    if request.method == "GET":
        departments = Department.objects.all().order_by("-created_at")
        items_in_page = 5
        paginator = Paginator(departments, items_in_page)

        page = request.GET.get('page')
        try:
            departments = paginator.page(page)
        except PageNotAnInteger:
            departments = paginator.page(1)
        except EmptyPage:
            departments = paginator.page(paginator.num_pages)

        context = {"departments": departments, "current_page": "departments"}
        return render(request, "list.html", context)

    elif request.method == "POST":
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
                return JsonResponse({"success": True})
            except Exception as e:
                return JsonResponse(
                    {"error_message": f"Error saving department: {e}"}, status=500
                )


# @login_required
@require_http_methods(["GET", "PUT", "PATCH", "DELETE"])
def department_detail(request, department_id):
    department = get_object_or_404(Department, id=department_id)

    if request.method == "GET":
        employees = Employee.objects.filter(department=department)
        context = {'employees': employees, 'department': department}
        return render(request, 'employee_list.html', context)

    elif request.method == "PATCH":
        # Update the department with the data from the request
        data = request.POST if request.method == "PATCH" else request.PUT
        department.name = data.get("name", department.name)
        department.description = data.get("description", department.description)

        try:
            department.save()
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"error_message": f"Error updating department: {e}"}, status=500)

    elif request.method == "DELETE":
        try:
            department.delete()
            return JsonResponse({"success": True})
        except Exception as e:
            return JsonResponse({"error_message": f"Error deleting department: {e}"}, status=500)
