from django.shortcuts import redirect, render
from app.form.create_ticket_form import CreateTicketForm
from django.contrib.auth.decorators import login_required
from app.models.ticket import Ticket  # Assurez-vous d'importer le modèle Ticket
from app.models.review import Review 

@login_required
def create_ticket(request):
    if request.method == 'POST':
        create_ticket_form = CreateTicketForm(request.POST, request.FILES)
        if create_ticket_form.is_valid():
            # Créer le Ticket
            ticket = Ticket.objects.create(
                user=request.user,
                title=create_ticket_form.cleaned_data['title'],
                description=create_ticket_form.cleaned_data['description'],
                image=create_ticket_form.cleaned_data['image']
            )
            # Créer la Review
            review = Review.objects.create(
                user=request.user,
                ticket=ticket,
                rating=create_ticket_form.cleaned_data['rating'],
                headline=create_ticket_form.cleaned_data['headline'],
                body=create_ticket_form.cleaned_data['body']
            )
            return redirect('app:flux')
    else:
        create_ticket_form = CreateTicketForm()

    context = { 'create_ticket_form': create_ticket_form }
    return render(request, "app/flux/create_ticket.html", context)