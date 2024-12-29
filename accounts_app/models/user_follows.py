from django.db import models
from backend.settings import AUTH_USER_MODEL


class UserFollows(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following")
    followed_user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="followed_by")

    class Meta:
        unique_together = ("user", "followed_user")

    def __str__(self):
        return f"{self.user} follows {self.followed_user}"