from django import forms


class CreateTicketForm(forms.Form):
    # Champs du modèle Ticket
    title = forms.CharField(max_length=128, label="Titre")  # Label pour le champ title
    description = forms.CharField(
        widget=forms.Textarea, max_length=2048, required=False, label="Description"  # Label pour le champ description
    )
    image = forms.ImageField(required=False, label="Image")  # Label pour le champ image

    # Champs du modèle Review
    rating = forms.ChoiceField(
        choices=[(i, i) for i in range(0, 6)],
        widget=forms.RadioSelect,
        label="Évaluation",  # Label pour le champ rating
    )
    headline = forms.CharField(max_length=128, label="Titre de la critique")  # Label pour le champ headline
    body = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 40}),
        required=False,
        label="Corps de la critique",  # Label pour le champ body
    )