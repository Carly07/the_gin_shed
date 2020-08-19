// Initialize and add the map
function initMap() {
  // The location of The Gin Shed
  var ginshed = {lat: 53.1897947, lng: -2.896595};
  // The map, centered at The Gin Shed
  var map = new google.maps.Map(
      document.getElementById('map'), {zoom: 9, center: ginshed});
  // The marker, positioned at The Gin Shed
  var marker = new google.maps.Marker({position: ginshed, map: map});
}