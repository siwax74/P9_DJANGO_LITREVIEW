from django.shortcuts import redirect
from app.forms.request_ticket_form import RequestTicketForm
from app.models.ticket import Ticket
from django.contrib.auth.decorators import login_required


@login_required
def create_ticket(request):
    if request.method == "POST":
        # Créer une instance de formulaire avec POST et FILES
        request_ticket_form = RequestTicketForm(request.POST, request.FILES)
        if request_ticket_form.is_valid():
            # Récupérer les données du formulaire
            title = request_ticket_form.cleaned_data["title"]
            description = request_ticket_form.cleaned_data["description"]
            image = request_ticket_form.cleaned_data["image"]

            Ticket.objects.create(
                user=request.user,
                title=title,
                description=description,
                image=image,
            )
            return redirect("app:flux")
