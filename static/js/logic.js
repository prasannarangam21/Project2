// Creating map object
var myMap = L.map("map", {
  center: [34.0522, -118.2437],
  zoom: 3,
  layer: greymap
});

// Adding tile layer
var greymap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
}).addTo(myMap);

// Store our API endpoint as queryUrl
//var queryUrl = "http://127.0.0.1:5000/api/suicides_by_country";


// Perform a GET request to the query URL
d3.json("http://127.0.0.1:5000/api/suicides_by_country", function (data) {
  console.log(data);


  function radius(suicides) {
    if (suicides === 0) {
      return 1;
    }
    return suicides;
  }

  function color(suicides) {
    switch (true) {
      case suicides >= 100000:
        return '#b6003b';
      case suicides >= 10000:
        return '#e52c00';
      case suicides >= 1000:
        return '#fe522a';
      case suicides >= 100:
        return '#fe9882';
      default:
        return '#ffded5';

    }
  }

  function circleStyle(feature) {
    return {
      fillColor: color(feature.properties.suicides),
      radius: radius(feature.properties.suicides),
      fillOpacity: 1,
      weight: 0.5,
      stroke: true
    };
  }

  // Add legend to the map
  var legend = L.control({ position: 'bottomright' });

  legend.onAdd = function (map) {

    var div = L.DomUtil.create('div', 'info legend'),
      suicides = [0, 10, 100, 1000, 10000, 100000];

    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < suicides.length; i++) {

      div.innerHTML +=
        "<i style='background:" + color(suicides[i]) + "'></i> " +
        suicides[i] + (suicides[i + 1] ? "&ndash;" + suicides[i + 1] + "<br>" : "+");
    }

    return div;
  };

  legend.addTo(myMap);

  var suicideLayer = L.geoJSON(data, {

    pointToLayer: function (feature, latlng) {
      return L.circleMarker(latlng);
    },
    style: circleStyle,
    // Give each feature a popup describing with information pertinent to it
    onEachFeature: function (feature, layer) {
      layer.bindPopup(`<h3>${feature.properties.country}</h3><hr/><p>${feature.properties.suicides}</p>`)
    }
  })

  suicideLayer.addTo(myMap);

});
