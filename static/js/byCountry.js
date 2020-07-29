 // Suicides by Country
 d3.json('/api/suicides_by_TopTenCountry').then(function(data){
    
  // Sort the objects in ascending order
  let sortedlist = Object.entries(data).sort((a, b) => a[1] - b[1]);
  console.log(sortedlist)

  var keys = []
  var values = []

  sortedlist.forEach(country=>{
    keys.push(country[0]);
    values.push(country[1])
  })
  
  var data = [
    {
      type: 'bar',
      x: values,
      y: keys,
      orientation: "h"
    },
  ];
  var layout = {
      title: "Countries with the highest suicide rates",
      autosize: false,
      width: 600,
      height: 600,
      margin: {
        l: 150,
        r: 50,
        b: 100,
        t: 100,
        pad: 4
      }
  }
  var config = {responsive: true}
  Plotly.newPlot('bar_by_country', data, layout, config);
});

// Suicides by Country
d3.json('/api/suicides_by_country').then(function(data){
  
  // Sort the objects in descending order
  let sortedlist = Object.entries(data).sort((a, b) => b[1] - a[1]);

  var keys = []
  var values = []

  sortedlist.forEach(country=>{
    keys.push(country[0]);
    values.push(country[1])
  })

  var data = [
    {
      type: 'bar',
      x: keys,
      y: values
    },
  ];
  var layout = {
      title: "Suicides by Country",
      autosize: false,
      width: 800,
      height: 500,
      margin: {
        l: 150,
        r: 50,
        b: 100,
        t: 100,
        pad: 4
      }
  }
  var config = {responsive: true}
  Plotly.newPlot('bar_by_country_all', data, layout, config);
});