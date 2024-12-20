from django import forms


class CreateReviewForm(forms.Form):
    # Champs du modèle Ticket
    title = forms.CharField(max_length=128, label="Titre")
    description = forms.CharField(widget=forms.Textarea, max_length=2048, required=False, label="Description")
    image = forms.ImageField(required=False, label="Image")

    # Champs du modèle Review
    rating = forms.ChoiceField(
        choices=[(i, i) for i in range(0, 6)],
        widget=forms.RadioSelect,
        label="Évaluation",
    )
    headline = forms.CharField(max_length=128, label="Titre")
    body = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 40}),
        required=False,
        label="Commentaire",
    )
