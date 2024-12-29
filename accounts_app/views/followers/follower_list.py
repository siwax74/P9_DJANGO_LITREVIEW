from itertools import chain
from django.shortcuts import render
from accounts_app.forms.research_user_form import UserSearchForm
from accounts_app.models.user_follows import UserFollows

def followers_list(request):
    title_view = "Abonnements"
    user = request.user
    followed_user = UserFollows.objects.filter(user=user)
    research_user_form = UserSearchForm()
    context = {'followed_user': followed_user,
               'title_view': title_view,
               'research_user_form': research_user_form}
    return render(request, "accounts_app/followers_list.html", context)