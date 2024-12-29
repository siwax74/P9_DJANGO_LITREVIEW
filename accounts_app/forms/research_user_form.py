from django import forms


class UserSearchForm(forms.Form):
    email = forms.EmailField(label="Adresse e-mail", max_length=150)
