from itertools import chain
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from accounts_app.forms.research_user_form import UserSearchForm
from accounts_app.models.user import Customer
from accounts_app.models.user_follows import UserFollows


def followers_list(request):
    title_view = "Abonnements"
    user = request.user
    followed_user = UserFollows.objects.filter(user=user)
    research_user_form = UserSearchForm()

    context = {"followed_user": followed_user, "title_view": title_view, "research_user_form": research_user_form}
    return render(request, "accounts_app/followers_list.html", context)


def search_user(request):
    if request.method == "POST":
        research_user_form = UserSearchForm(request.POST)
        if research_user_form.is_valid():
            user = request.user
            research_user_email = research_user_form.cleaned_data["email"]

            try:
                followed_user = Customer.objects.get(email=research_user_email)

                if user.email == followed_user.email:
                    return HttpResponse("Impossible de vous suivre vous même !", status=400)

                if UserFollows.objects.filter(user=user, followed_user=followed_user).exists():
                    return HttpResponse("Vous suivez déjà cet utilisateur .", status=400)

                UserFollows.objects.create(user=user, followed_user=followed_user)
                return HttpResponse("Success", status=200)
            except Customer.DoesNotExist:
                return HttpResponse("Utilisateur non trouvé !", status=404)
            except Exception as e:
                return HttpResponse("Erreur !", status=500)
        else:
            return HttpResponse("Veuillez entrer un Email valide !", status=400)
