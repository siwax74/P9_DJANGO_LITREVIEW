from django import forms
class CreateTicketForm(forms.Form):

    # Champs du modèle Ticket
    title = forms.CharField(max_length=128)
    description = forms.CharField(widget=forms.Textarea, max_length=2048, required=False)
    image = forms.ImageField(required=False)

    # Champs du modèle Review
    rating = forms.ChoiceField(choices=[(i, i) for i in range(0, 6)], widget=forms.RadioSelect)
    headline = forms.CharField(max_length=128)
    body = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'cols': 40}), required=False)