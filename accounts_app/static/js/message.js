const messageElements = document.querySelectorAll(".messages");

function removeMessage(element) {
  setTimeout(() => {
    element.remove(); // Supprime l'élément du DOM
  }, 3000); // 3000 millisecondes = 3 secondes
}

// Appliquer la fonction à chaque message
messageElements.forEach(removeMessage);
