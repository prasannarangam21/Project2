$.ajax({
    dataType: "json",
    url: '/api/suicides_by_generation',
    data: {},
    success: function(data){
      console.log(data);
      var labels = Object.keys(data)
      var values = Object.values(data)
      var trace = {
          type: 'pie',
          labels: labels,
          values: values
      }   
      var layout = {
            title:'Suicide Rates by Generation',
            width: 600,
            height: 600
      }
      Plotly.newPlot('pie_generation', [trace], layout);
    }
});

