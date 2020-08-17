$(document).ready(function () {

    /**
     * Set copyright date to current year 
     */

    $('#copyright-year').text(new Date().getFullYear());
});


// Initialize and add the map
function initMap() {
  // The location of Uluru
  var uluru = {lat: 53.1897947, lng: -2.896595};
  // The map, centered at Uluru
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 9, center: uluru});
  // The marker, positioned at Uluru
  var marker = new google.maps.Marker({position: uluru, map: map});
}