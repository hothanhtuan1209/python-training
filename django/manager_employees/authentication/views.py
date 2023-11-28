from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def user_login(request):
    """
    This is function to login and authenticate user
    """

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('user_logout')

        else:
            return render(
                request, 'login.html', {'error': 'Invalid login credentials'}
            )

    else:
        return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('user_login')
