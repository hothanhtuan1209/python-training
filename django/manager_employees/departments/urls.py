from django.urls import path
from .views import departments, department_detail

urlpatterns = [
    path('', departments, name='departments'),
    path('<uuid:department_id>', department_detail, name="department_detail"),
]
