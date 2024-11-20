from django.urls import path

from accounts_app.views.logout import logout_user
from accounts_app.views.signup import signup
from accounts_app.views.login import login_user

app_name = "accounts_app"

urlpatterns = [
    path("signup/", signup, name="signup"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
]