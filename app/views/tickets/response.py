from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from app.form.create_ticket_form import CreateTicketForm
from app.models.ticket import Ticket

@login_required
def ticket_detail(request, ticket_id):
    title_view = "Critique"
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        create_ticket_form = CreateTicketForm(request.POST, request.FILES)
        if create_ticket_form.is_valid():
            # Traitez les données du formulaire ici
            # Par exemple, vous pouvez sauvegarder les données que vous souhaitez
            # ticket.some_field = create_ticket_form.cleaned_data['some_field']
            # ticket.save()
            pass  # Remplacez ceci par votre logique de traitement
    else:
        create_ticket_form = CreateTicketForm()  # Créez un formulaire vide pour les requêtes GET

    print(ticket)
    return render(request, 'app/tickets/response.html', {
        'create_ticket_form': create_ticket_form,
        'ticket': ticket,
        'title_view': title_view
    })