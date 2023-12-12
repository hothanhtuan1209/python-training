from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Department


@login_required
def departments(request):
    """
    This function get a list of departments from the database.
    """

    departments = Department.objects.all().order_by("-created_at")[:10]
    context = {"departments": departments, "current_page": "departments"}
    return render(request, "list.html", context)
