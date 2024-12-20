from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from app.forms.response_review_form import ResponseReviewForm
from app.forms.request_ticket_form import RequestTicketForm
from app.models.review import Review
from app.models.ticket import Ticket


def post_update(request, post_id):
    title_view = "Modification"

    # Tentez de récupérer le ticket ou la critique
    ticket = Ticket.objects.filter(id=post_id, user=request.user).first()
    review = Review.objects.filter(id=post_id, user=request.user).first()

    if not ticket and not review:
        return JsonResponse({"error": "Post not found or not accessible"}, status=404)

    post = ticket if ticket else review
    action_url = reverse("app:post-update", args=[post_id])

    if request.method == "POST":
        if ticket:
            form = RequestTicketForm(request.POST, instance=ticket)
        else:
            form = ResponseReviewForm(request.POST, instance=review)

        if form.is_valid():
            form.save()
            return redirect("app:flux")
    else:
        request_ticket_form = RequestTicketForm(instance=ticket) if ticket else None
        review_form = ResponseReviewForm(instance=review) if review else None
        context = {
            "request_ticket_form": request_ticket_form,
            "review_form": review_form,
            "title_view": title_view,
            "post": post,
            "action_url": action_url,
        }
        return render(request, "app/posts/post_update.html", context)
