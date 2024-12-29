from django import forms

class UserSearchForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur', max_length=150)