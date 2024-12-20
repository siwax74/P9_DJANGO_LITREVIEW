from django import forms

from app.models.review import Review


class ResponseReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ["headline", "rating", "body"]
        widgets = {
            "rating": forms.RadioSelect(attrs={"empty_label": None}),
        }
        labels = {
            "headline": "Titre",
            "rating": "Note",
            "body": "Commentaire",
        }
