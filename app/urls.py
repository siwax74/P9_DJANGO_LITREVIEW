from django.urls import path
from app.views.posts.post_delete import post_delete
from app.views.posts.post_list import post_list

from app.views.posts.post_update import post_update
from app.views.tickets.show_ticket_form import show_ticket_form
from app.views.tickets.create_ticket import create_ticket

from app.views.reviews.show_review_form import show_review_form
from app.views.reviews.create_review import create_review

from app.views.reviews.response import ticket_detail

from app.views.flux.flux import flux
from app.views.home import home


app_name = "app"

urlpatterns = [
    path("", home, name="home"),
    path("flux/", flux, name="flux"),
    path("show_ticket_form/", show_ticket_form, name="show-ticket-form"),
    path("create_ticket/", create_ticket, name="create-ticket"),
    path("show_review_form/", show_review_form, name="show-review-form"),
    path("create_review/", create_review, name="create-review"),
    path("post_update/<int:post_id>/", post_update, name="post-update"),
    path("post_list/", post_list, name="post-list"),
    path("post/<int:post_id>/delete/", post_delete, name="post-delete"),
    path("ticket/<int:ticket_id>/", ticket_detail, name="ticket-detail"),
]
