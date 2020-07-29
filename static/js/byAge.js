// Suicides by Age

function plotBubble(labels, values,markerSize){

  var trace1 = {
    x: labels,
    y: values,
    mode: 'markers',
    marker: {
      size: markerSize,
      color: values,
      colorscale: [
            ['0.0', 'rgb(165,0,38)'],
            ['0.111111111111', 'rgb(215,48,39)'],
            ['0.222222222222', 'rgb(244,109,67)'],
            ['0.333333333333', 'rgb(253,174,97)'],
            ['0.444444444444', 'rgb(254,224,144)'],
            ['0.555555555556', 'rgb(224,243,248)'],
            ['0.666666666667', 'rgb(171,217,233)'],
            ['0.777777777778', 'rgb(116,173,209)'],
            ['0.888888888889', 'rgb(69,117,180)'],
            ['1.0', 'rgb(49,54,149)']
          ],
    }  
  }
  var data = [trace1];
  var layout = {
      width: 600,
      height: 600,
      xaxis: {
          title: 'Age Group'
      },
      yaxis: {
          title: 'Suicides'
      },
      title: 'Suicides by Age'
  }
  var config = {responsive: true}

  Plotly.newPlot("bubble_age", data, layout, config);
}

d3.json('/api/suicides_by_age').then(function(data){
  console.log(data)
  var bubbleLabels = Object.keys(data)
  var bubbleValues = Object.values(data)  
  var bubbleSize = bubbleValues.map(x=>x/20000)
  plotBubble(bubbleLabels,bubbleValues,bubbleSize)
});

// Add click event to plot the pie chart for the selected year
$('.btn').click(function(){
  event.preventDefault();
  const year = $('#inputYear').val()
  console.log("year ",year)

  d3.json('/api/yearly_suicides_by_age').then(function(data){
      console.log("yearly",data)
      var selected_output
      Object.entries(data).forEach(function([key,value]){
          if (key==year){
              selected_output = value
          }
      })
      
      var labels = []
      var values = []
      selected_output.forEach(output => {
          labels.push(output.age)
          values.push(output.suicides)
      })
      var markerSize = values.map(x=>x/500)
      plotBubble(labels, values, markerSize)
  })
})

d3.json('/api/yearly_suicides_by_age').then(function(data){
    
  // var year = [];
  // var Age1 = [];
  // var Age2 = [];
  // var Age3 = [];
  // var Age4 = [];
  // var Age5 = [];
  // var Age6 = [];
  // Object.entries(data).forEach(function([key,value]){
  //     year.push(key);
  //     value.forEach(v=>{
  //         if (v.age == "5-14 years"){
  //           Age1.push(v.suicides);
  //         } else if (v.age == "15-24 years"){
  //           Age2.push(v.suicides);
  //         } else if (v.age == "25-34 years"){
  //           Age3.push(v.suicides);
  //         } else if (v.age == "35-54 years"){
  //           Age4.push(v.suicides);
  //         } else if (v.age == "55-74 years"){
  //           Age5.push(v.suicides);
  //         }else {
  //           Age6.push(v.suicides);
  //         }
  //     })
  // })

  var year = [];
  var Age = [];
  Object.entries(data).forEach(function([key,value]){
      year.push(key);
      value.forEach(v=>{
          if (v.age == "35-54 years"){
            Age.push(v.suicides);
          } 
      })
  })
  var data = [
    {
      type: 'bar',
      x: year,
      y: Age,
      marker:{
        color: '#FF7F50'
      }
    },
  ];
  var layout = {
      title: "Suicides for Age '35-54 Years'",
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
  Plotly.newPlot('bubble_certainAgeGroup', data, layout, config);
})