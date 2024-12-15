from django.urls import path
from app.views.create_ticket import create_ticket
from app.views.request_ticket import request_ticket
from app.views.flux import flux
from app.views.home import home

app_name = "app"

urlpatterns = [
    path("", home, name="home"),
    path("flux/", flux, name="flux"),
    path("request_ticket/", request_ticket, name="request-ticket"),
    path("create_ticket/", create_ticket, name="create-ticket"),
]