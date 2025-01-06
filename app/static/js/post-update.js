document.addEventListener('DOMContentLoaded', function() {
    let postRequest = document.querySelector('.post-request');
    if (postRequest) {
        postRequest.textContent = "Vous êtes en train de répondre en réponse à ";
    }

    let postDate = document.querySelector('.post-date');
    if (postDate) {
        postDate.remove();
    }

    let postReviewRow = document.querySelector('.post-review-row');
    if (postReviewRow) {
        postReviewRow.remove();
    }

    let postDescription = document.querySelector('.post-description');
    if (postDescription) {
        postDescription.remove();
    }

    let downloadingImage = document.querySelector('.downloading-image');
    if (downloadingImage) {
        downloadingImage.querySelectorAll('a, label, input[type="checkbox"]').forEach(element => element.remove());
    }
});