from itertools import chain
from django.shortcuts import render
from app.models.review import Review
from app.models.ticket import Ticket
from django.contrib.auth.decorators import login_required


@login_required
def post_list(request):
    title_view = "Vos posts"
    user = request.user
    tickets_user = Ticket.objects.filter(user=user)
    reviews_user = Review.objects.filter(user=user)
    posts = sorted(
        chain(tickets_user, reviews_user),
        key=lambda post: post.time_created,
        reverse=True,
    )
    return render(request, "app/posts/post_list.html", {"posts": posts, "title_view": title_view})
