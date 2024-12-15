from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from app.models.ticket import Ticket
from backend.settings import AUTH_USER_MODEL

class Review(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    ticket=models.ForeignKey(Ticket, on_delete=models.CASCADE, blank=True)
    rating=models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    headline = models.CharField(max_length=128)
    body = models.TextField(max_length=8192, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.headline}, {self.user}, {self.time_created} - Rating: {self.rating}/5"    

    def as_dict(self):
            """
            Convert the Review instance to a dictionary.
            """
            return {
                "id": self.id,
                "user": self.user if self.user else None,
                "ticket_id": self.ticket if self.ticket else None,
                "rating": self.rating,
                "headline": self.headline,
                "body": self.body,
                "time_created": self.time_created,
            }