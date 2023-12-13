from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def user_login(request):
    """
    This is function to login and authenticate user
    """

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("departments")

        else:
            return render(
                request,
                "login.html",
                {"error": "Username or password is incorrect, please re-enter"},
            )

    else:
        return render(request, "login.html")


@login_required
def user_logout(request):
    """
    Logout the user and redirect to the login page.
    """

    logout(request)
    return redirect("user_login")
