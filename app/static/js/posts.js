document.addEventListener('DOMContentLoaded', () => {
    // Fonction pour récupérer le token CSRF
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Vérifiez si ce cookie commence par le nom que nous cherchons
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    // Récupérer le token CSRF depuis les cookies
    const csrfToken = getCookie('csrftoken');

    // Ajouter l'événement de suppression pour chaque bouton
    document.querySelectorAll('.btn-delete').forEach(button => {
        button.addEventListener('click', () => {
            const deleteUrl = button.dataset.url;
            if (confirm("Êtes-vous sûr de vouloir supprimer ce post ?")) {
                fetch(deleteUrl, {
                    method: 'POST',
                    headers: {
                        'X-CSRFToken': csrfToken,
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({})
                })
                .then(response => response.json())
                .then(data => {
                    if (data.success) {
                        alert(data.success);
                        location.reload();
                    } else {
                        alert(data.error);
                    }
                })
                .catch(err => console.error(err));
            }
        });
    });
});