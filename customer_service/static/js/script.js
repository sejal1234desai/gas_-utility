// Sample script to show an alert when a form is submitted
document.addEventListener('DOMContentLoaded', function () {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function (event) {
            alert('Form submitted successfully!');
        });
    }
});
