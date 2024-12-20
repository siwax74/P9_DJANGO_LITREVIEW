from django.shortcuts import render
from django.urls import reverse
from app.forms.request_ticket_form import RequestTicketForm
from django.contrib.auth.decorators import login_required


@login_required
def show_ticket_form(request):
    title_view = "Ticket"
    action_url = reverse("app:create-ticket")
    request_ticket_form = RequestTicketForm()
    context = {"request_ticket_form": request_ticket_form, "title_view": title_view, "action_url": action_url}
    return render(request, "app/tickets/show_ticket_form.html", context)
