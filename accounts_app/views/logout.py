from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


@login_required
def logout_user(request):
    logout(request)
    return redirect("app:home")
