from django import forms


class UserSearchForm(forms.Form):
    username = forms.CharField(
        max_length=10, label="", widget=forms.TextInput(attrs={"placeholder": "Entrez le nom d'utilisateur"})
    )
