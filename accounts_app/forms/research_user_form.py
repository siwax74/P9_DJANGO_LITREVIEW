from django import forms


class UserSearchForm(forms.Form):
    email = forms.EmailField(
        max_length=150, label="", widget=forms.EmailInput(attrs={"placeholder": "Entrez l'email de l'utilisateur"})
    )
