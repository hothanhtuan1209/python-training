from django.shortcuts import render
from django.contrib.auth.decorators import login_required
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
