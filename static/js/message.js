const messageElements = document.querySelectorAll(".messages");

function removeMessage(element) {
  setTimeout(() => {
    element.remove();
  }, 3000);
}

// Appliquer la fonction à chaque message
messageElements.forEach(removeMessage);
