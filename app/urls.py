from django.urls import path
from app.views.reviews.create import create_ticket
from app.views.tickets.response import ticket_detail
from app.views.tickets.create import request_ticket
from app.views.flux.flux import flux
from app.views.home import home

app_name = "app"

urlpatterns = [
    path("", home, name="home"),
    path("flux/", flux, name="flux"),
    path("request_ticket/", request_ticket, name="request-ticket"),
    path("create_ticket/", create_ticket, name="create-ticket"),
    path("ticket/<int:ticket_id>/", ticket_detail, name="ticket-detail"),
]
