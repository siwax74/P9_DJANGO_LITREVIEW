from django.http import JsonResponse
from app.models.ticket import Ticket
from app.models.review import Review
from django.contrib.auth.decorators import login_required


@login_required
def post_delete(request, post_id):
    """Supprime un ticket ou une critique appartenant à l'utilisateur."""

    # Supprimer si méthode POST
    if request.method == "POST":
        try:
            # Tentez de récupérer le ticket ou la critique
            ticket = Ticket.objects.filter(id=post_id, user=request.user).first()
            review = Review.objects.filter(id=post_id, user=request.user).first()

            # Identifier le type de post
            post = ticket if ticket else review

            # Vérifiez si le post existe
            if not post:
                return JsonResponse({"error": "Post introuvable ou vous n'avez pas les permissions."}, status=404)
            post.delete()
            return JsonResponse({"success": "Post supprimé avec succès !"}, status=200)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
