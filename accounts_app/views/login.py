from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("app:flux")
        else:
            messages.info(request, "Email ou mot de passe incorrect")
    return render(request, "app/home.html")
