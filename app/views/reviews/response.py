from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from app.forms.response_review_form import ResponseReviewForm
from app.models.review import Review
from app.models.ticket import Ticket
from django.contrib import messages


@login_required
def ticket_detail(request, ticket_id):
    title_view = "Critique"
    ticket = get_object_or_404(Ticket, id=ticket_id)

    # Vérifier si une critique existe déjà pour ce ticket
    if Review.objects.filter(ticket=ticket).exists():
        messages.error(request, "Une critique a déjà été faite sur ce ticket.")
        return redirect("app:flux")

    if request.method == "POST":
        review_form = ResponseReviewForm(request.POST)
        if review_form.is_valid():
            # Créer un objet Review en utilisant le ticket existant
            review = review_form.save(commit=False)
            review.ticket = ticket
            review.user = request.user
            review.save()
            return redirect("app:flux")
    else:
        review_form = ResponseReviewForm()

    return render(
        request,
        "app/reviews/response.html",
        {
            "review_form": review_form,
            "ticket": ticket,
            "title_view": title_view,
        },
    )
