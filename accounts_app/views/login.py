from django.contrib.auth import login, authenticate
from django.shortcuts import redirect, render
from django.contrib import messages


def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("app:flux")
        else:
            messages.add_message(request, messages.ERROR, "Nom d'utilisateur ou mot de passe incorect !")
    return render(request, "app/home.html")