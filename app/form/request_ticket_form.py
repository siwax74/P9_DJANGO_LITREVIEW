from django import forms
from app.models.ticket import Ticket


class RequestTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ["title", "description", "image"]
