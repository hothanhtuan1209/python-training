from django.urls import path
from .views import departments, create_department

urlpatterns = [
    path('', departments, name='departments'),
    path('new/', create_department, name='create_department'),
]
