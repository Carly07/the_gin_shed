
// Set copyright date to current year
$(document).ready(function () {
    $('#copyright-year').text(new Date().getFullYear());
});


// Set timeout on messages container
setTimeout(function () {
    $('#msg-container').fadeOut('slow');
}, 4000);