from django.urls import path
from .views import departments_list

urlpatterns = [
    path('deparments/departments_list', departments_list, name='departments_list')
]