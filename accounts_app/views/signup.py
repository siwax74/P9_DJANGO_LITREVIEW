from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from accounts_app.models.user import Customer

User = get_user_model()


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        try:
            if len(username) > 10:
                messages.add_message(request, messages.ERROR, "Le nom d'utilisateur ne doit pas dépasser 10 caractères.")
                return render(request, "accounts_app/signup.html")
            if password != password1:
                messages.add_message(request, messages.ERROR, "Les mots de passe ne correspondent pas.")
            user = Customer.objects.get(username=username)
            messages.add_message(request, messages.ERROR, "Un compte utilisateur existe déjà.")
        except Customer.DoesNotExist:
            if password == password1:
                user = Customer.objects.create_user(username=username, password=password)
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect("app:flux")
    return render(request, "accounts_app/signup.html")
