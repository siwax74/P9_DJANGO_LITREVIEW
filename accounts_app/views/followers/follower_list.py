from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from accounts_app.forms.research_user_form import UserSearchForm
from accounts_app.models.user import Customer
from accounts_app.models.user_follows import UserFollows
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model


@login_required
def followers_list(request):
    title_view = "Abonnements"
    user = request.user

    followed_user = UserFollows.objects.filter(user=user)

    followers = UserFollows.objects.filter(followed_user=user)

    research_user_form = UserSearchForm()

    context = {
        "followed_user": followed_user,
        "followers": followers,
        "title_view": title_view,
        "research_user_form": research_user_form,
    }
    return render(request, "accounts_app/followers_list.html", context)


@login_required
def search_user(request):
    if request.method == "POST":
        research_user_form = UserSearchForm(request.POST)
        if research_user_form.is_valid():
            user = request.user
            research_user = research_user_form.cleaned_data["username"]

            try:
                followed_user = Customer.objects.get(username=research_user)

                if user.username == followed_user.username:
                    return HttpResponse("Impossible de vous suivre vous même !", status=400)

                if UserFollows.objects.filter(user=user, followed_user=followed_user).exists():
                    return HttpResponse("Vous suivez déjà cet utilisateur .", status=400)

                UserFollows.objects.create(user=user, followed_user=followed_user)
                return HttpResponse("Success", status=200)
            except Customer.DoesNotExist:
                return HttpResponse("Utilisateur non trouvé !", status=404)
        else:
            return HttpResponse("Veuillez entrer un username valide !", status=400)


@login_required
def unfollow(request):
    if request.method == "POST":
        followed_user_id = request.POST.get("unfollow")
        User = get_user_model()
        followed_user = get_object_or_404(User, id=followed_user_id)
        UserFollows.objects.filter(user=request.user, followed_user=followed_user).delete()
        return redirect("app:flux")
    return redirect("app:flux")
