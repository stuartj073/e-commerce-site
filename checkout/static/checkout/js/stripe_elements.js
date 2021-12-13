// connecting to the Stripe server

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(-1, 1);
var stripe = Stripe(stripePublicKey);  // set up stripe
var elements = stripe.elements();  // prebuilt UI components from Stripe
var card = elements.create('card');
card.mount('#card-element');


// Handle realtime validation errors on the card element

card.addEventListener('click', function(event){
    var errorDiv = document.getElementById('card-errors')
    if (event.error){
        var html = `
                   <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                   </span>
                   <span>${event.error.message}</span>
                   `;
                   $(errorDiv).html(html);
                } else {
                    errorDiv.textContent = '';
                }
});

// Handle form Submit

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev){
    ev.preventDefault();
    card.update({'disabled': true});  // prevent multiple submissions
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function(result){
        if (result.error){
        var html = `
            <span class="icon" role="alert">
             <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>
            `;
        $(errorDiv).html(html);
        $('#payment-form').fadeToggle(100);
        $('#loading-overlay').fadeToggle(100);
        card.update({ 'disabled': false});  // re-enable card-update, submit
        $('#submit-button').attr('disabled', false);  
        } else {
            // The payment was successful
            if (result.paymentIntent.status == 'succeeded'){
                form.submit()
            }
        }
    })
})