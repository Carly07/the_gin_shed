$(document).ready(function () {

    /**
     * Set copyright date to current year 
     */

    $('#copyright-year').text(new Date().getFullYear());
});

// history back function for Keep shopping button product detail page 
// so user can return to their previous search results

function goBack() {
  window.history.go(-1);
}
