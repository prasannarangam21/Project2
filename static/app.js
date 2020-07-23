
d3.json('/api/suicides_by_gender').then(function (data) {
  console.log('countrydata', data)
  var keys = Object.keys(data)
  var values = Object.values(data)
  var trace = {
    type: 'pie',
    labels: keys,
    values: values
  }
  Plotly.newPlot('pie', [trace]);

});





