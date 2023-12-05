from django.urls import path
from .views import departments_list

urlpatterns = [
    path('departments', departments_list, name='departments_list')
]
