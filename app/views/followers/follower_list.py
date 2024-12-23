from itertools import chain
from django.shortcuts import render
from app.models.review import Review
from app.models.ticket import Ticket
from app.models.user_follows import UserFollows

def followers_list(request):

    user = request.user
    followed_user = UserFollows.objects.filter(user=user)
    