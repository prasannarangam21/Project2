// Load the data and Data Cleaning - d3.json (api)
d3.json('/api/suicides_by_gender').then(function(data){
    // console.log(data) 
    var labels = Object.keys(data)
    var values = Object.values(data)
    var trace = {
        type: 'pie',
        labels: labels,
        values: values
    }   
    var layout = {
        title:'Suicide Rates by Gender'
    }
    Plotly.newPlot('pie', [trace], layout);
});



d3.json('/api/suicides_and_gdp').then(function(data){
   
    var countries = []
    var suicides = []
    var gdp = []

    Object.entries(data).forEach(function([key,value]){
        countries.push(key);
        suicides.push(value.suicides);
        gdp.push(value.gdp)
    })
    
    var trace1 = {
        x: gdp,
        y: suicides,
        mode: 'markers',
        type: 'scatter',
        name: 'Suicides vs GDP',
        text: countries,
        marker: { size: 12 }
      };
    
    var data = [trace1];
    
    var layout = {
        xaxis: {
            title: 'gdp per capita'
        },
        yaxis: {
            title: 'suicides rates per 100k'
        },
        title:'Suicides vs GDP'
    };
    
    Plotly.newPlot('scatter1', data, layout);
});



d3.json("/api/suicides_by_country").then(function(data){
    
    var data = [
        {
          x: Object.keys(data),
          y: Object.values(data),
          type: 'bar'
        }
      ];
      
      Plotly.newPlot('bar', data);
})



d3.json('/api/suicides_per_100k_by_year').then(function (data) {
    var gd = document.getElementById('lineDiv');
    var data = [{mode: 'lines',
    x:Object.keys(data),
    y:Object.values(data)}]
    var layout = {margin: {l: 150}, width:600, height: 500,
    title: "Average number of suicides per 100K population from 1997 to 2014"}
    Plotly.newPlot('lineDiv', data, layout);
});



// Suicides by Age
d3.json('/api/suicides_by_age').then(function(data){
    console.log(data);
    var ageLabels = Object.keys(data)
    var ageValues = Object.values(data)
    console.log(ageLabels,ageValues);
    var trace1 = {
      type: "scatter",
      mode: "markers",
      x: ageLabels,
      y: ageValues
    }
    Plotly.newPlot("scatter", [trace1]);
  });