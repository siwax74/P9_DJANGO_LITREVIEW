from django.contrib import admin
from .models import Review, Ticket, UserFollows


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("user", "ticket", "rating", "headline", "time_created")
    search_fields = ("headline", "body")
    list_filter = ("rating", "time_created")
    ordering = ("-time_created",)


class TicketAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "time_created")
    search_fields = ("title", "description")
    list_filter = ("time_created",)
    ordering = ("-time_created",)


class UserFollowsAdmin(admin.ModelAdmin):
    list_display = ("user", "followed_user")
    list_filter = ("user", "followed_user")
    ordering = ("user",)


# Enregistrement des modèles avec leurs classes d'administration
admin.site.register(Review, ReviewAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(UserFollows, UserFollowsAdmin)
