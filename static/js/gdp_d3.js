d3.json('/api/suicides_and_gdp').then(function(data){
   
    var countries = []
    var suicides = []
    var gdp = []

    Object.entries(data).forEach(function([key,value]){
        countries.push(key);
        suicides.push(value.suicides);
        gdp.push(value.gdp)
    })
    
    var corr = spearson.correlation.pearson(gdp, suicides);
    console.log(corr)
    
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
        width: 600,
        height: 600,
        xaxis: {
            title: 'gdp per capita'
        },
        yaxis: {
            title: 'suicides rates per 100k'
        },
        title:'Suicides vs GDP',
        annotations: [
          {
            x: 50000,
            y: 400,
            xref: 'x',
            yref: 'y',
            text: `Pearson Correlation: ${corr.toFixed(2)}`,
            showarrow: true,
            // arrowhead: 7,
            ax: 0,
            ay: -40
          }
        ]
    };
    
    var config = {responsive: true}

    Plotly.newPlot('scatter_gdp', data, layout, config)
});

d3.json('/api/yearly_suicides_and_gdp').then(function(data){
    console.log(data)

    var year = []
    var gdp = []
    var suicides = []
    Object.entries(data).forEach(([key,value])=>{
        year.push(key)
        gdp.push(value.gdp_per_capita)
        suicides.push(value.suicide_rates)
    })

    var trace1 = {
        x: year,
        y: suicides,
        name: 'Suicide Rates',
        type: 'scatter'
      };
      
      var trace2 = {
        x: year,
        y: gdp,
        name: 'GDP Per Capita',
        yaxis: 'y2',
        type: 'scatter'
      };
      
      var data = [trace1, trace2];
      
      var layout = {
        title: 'GDP and Suicide Rates Over Years',
        yaxis: {title: 'Suicide Per 100k'},
        yaxis2: {
          title: 'GDP Per Capita',
          titlefont: {color: 'rgb(148, 103, 189)'},
          tickfont: {color: 'rgb(148, 103, 189)'},
          overlaying: 'y',
          side: 'right'
        }
      };
      
      Plotly.newPlot('gdp_and_suicides_multiaxes', data, layout);
})