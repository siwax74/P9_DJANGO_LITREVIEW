from django import forms

from accounts_app.models.user import Customer


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Votre mot de passe'}))

    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "email", "password"]