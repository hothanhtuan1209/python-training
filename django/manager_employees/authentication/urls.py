from django.urls import path
from .views import user_login, user_logout, departments_list

urlpatterns = [
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('departments_list', departments_list, name='departments_list')
]
