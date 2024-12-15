from django.db import models

from backend.settings import AUTH_USER_MODEL

class Ticket(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2048, blank=True)
    image = models.ImageField(upload_to='articles', null=True, blank=True)
    time_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.user}, {self.time_created}"

    def as_dict(self):
        """
        Convert the Ticket instance to a dictionary.
        """
        return {
            "id": self.id,
            "user": self.user if self.user else None,
            "title": self.title,
            "description": self.description,
            "image": self.image.url if self.image else None,
            "time_created": self.time_created,
        }