from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.models.review import Review
from app.models.ticket import Ticket
from app.models.user_follows import UserFollows
from itertools import chain


@login_required
def flux(request):
    title_view = "Flux"
    user = request.user
    followed_users = UserFollows.objects.filter(user=user).values_list("followed_user", flat=True)

    # Récupérer les billets et critiques
    tickets_user = Ticket.objects.filter(user=user)
    reviews_user = Review.objects.filter(user=user)
    tickets_followed = Ticket.objects.filter(user__in=followed_users)
    reviews_followed = Review.objects.filter(user__in=followed_users)

    # Exclure les tickets qui ont déjà des reviews
    reviewed_ticket_ids = Review.objects.values_list("ticket_id", flat=True)
    tickets_user = tickets_user.exclude(id__in=reviewed_ticket_ids)
    tickets_followed = tickets_followed.exclude(id__in=reviewed_ticket_ids)

    # Combiner les résultats
    posts = sorted(
        chain(tickets_user, reviews_user, tickets_followed, reviews_followed),
        key=lambda post: post.time_created,
        reverse=True,
    )

    return render(request, "app/flux/flux.html", {"posts": posts, "title_view": title_view})
