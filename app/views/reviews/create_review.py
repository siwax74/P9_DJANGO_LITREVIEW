from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from app.forms.review_form import CreateReviewForm
from app.models.ticket import Ticket
from app.models.review import Review


@login_required
def create_review(request):
    user = request.user
    if request.method == "POST":
        create_ticket_form = CreateReviewForm(request.POST, request.FILES)
        if create_ticket_form.is_valid():
            # Extraction des données du formulaire
            title = create_ticket_form.cleaned_data["title"]
            description = create_ticket_form.cleaned_data["description"]
            image = create_ticket_form.cleaned_data.get("image", None)

            # Créer le Ticket
            ticket = Ticket.objects.create(
                user=user,
                title=title,
                description=description,
                image=image,
            )
            # Créer la Review
            Review.objects.create(
                user=user,
                ticket=ticket,
                rating=create_ticket_form.cleaned_data["rating"],
                headline=create_ticket_form.cleaned_data["headline"],
                body=create_ticket_form.cleaned_data["body"],
            )
            return redirect("app:flux")
