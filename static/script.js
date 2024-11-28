// script.js

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('expense-form');
    
    // Add event listener for form submission
    form.addEventListener('submit', function(event) {
        const amountInput = form.querySelector('input[name="amount"]');
        const amount = parseFloat(amountInput.value);
        
        // Basic validation for amount
        if (isNaN(amount) || amount <= 0) {
            event.preventDefault();  // Prevent form submission
            alert('Please enter a valid amount greater than zero.');
            amountInput.focus();  // Focus back on the amount input
        }
    });
});