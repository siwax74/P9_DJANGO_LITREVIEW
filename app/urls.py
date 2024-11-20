from django.urls import path

from app.views.home.home_view import home

app_name = "app"

urlpatterns = [
    path("", home, name="home"),
]