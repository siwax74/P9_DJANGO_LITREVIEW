document.addEventListener("DOMContentLoaded", function () {
    const btnAddUser  = document.getElementById('btn-add-user');
    const addUserForm = document.getElementById('add-user-form');

    btnAddUser .addEventListener("click", async function (event) {
        event.preventDefault();
        try {

            const formData = new FormData(addUserForm);
            const response = await fetch('/search_user/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCookie('csrftoken')
                }
            });

            if (!response.ok) {
                const errorText = await response.text();
                throw new Error(errorText);
            }
            // Success
            alert('Utilisateur suivi avec succès !');
            addUserForm.reset();
        } catch (error) {
            console.error('Erreur:', error);
            alert(`Erreur: ${error.message}`);
        }
    });

    // Function to retrieve the CSRF token
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Check if this cookie starts with the name we are looking for
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});