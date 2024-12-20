from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from app.forms.review_form import CreateReviewForm


@login_required
def show_review_form(request):
    title_view = "Critique"
    create_review_form = CreateReviewForm()
    context = {"create_review_form": create_review_form, "title_view": title_view}
    return render(request, "app/reviews/show_review_form.html", context)
