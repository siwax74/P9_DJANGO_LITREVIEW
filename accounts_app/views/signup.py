from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from accounts_app.models.user import Customer

User = get_user_model()


def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")
        try:
            if password != password1:
                messages.add_message(request, messages.ERROR, "Les mots de passe ne correspondent pas.")
            user = Customer.objects.get(email=email)
            messages.add_message(
                request, messages.ERROR, "Un compte utilisateur avec cette adresse email existe déjà."
            )
        except Customer.DoesNotExist:
            if password == password1:
                user = Customer.objects.create_user(
                    email=email, password=password, first_name=first_name, last_name=last_name
                )
                user = authenticate(request, email=email, password=password)
                login(request, user)
                return redirect("app:flux")
    return render(request, "accounts_app/signup.html")
