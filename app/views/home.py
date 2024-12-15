from django.shortcuts import redirect, render


def home(request):
    if request.user.is_authenticated:
        return redirect("app:flux")
    return render(request, "app/home.html")
