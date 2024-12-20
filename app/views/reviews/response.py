from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from app.forms.response_review_form import ResponseReviewForm
from app.models.ticket import Ticket


@login_required
def ticket_detail(request, ticket_id):
    title_view = "Critique"
    ticket = get_object_or_404(Ticket, id=ticket_id)

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
