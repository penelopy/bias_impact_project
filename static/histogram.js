$(function () {
    $('.myButton').on("click",
     function() {
      bias = event.target.dataset.bias;
      $.post("/bias", {bias: bias, gender: 'male'}, myFunc);
    });
  });

function myFunc(data){
  parsed_data = $.parseJSON(data);
  var menDataset = parsed_data[0];
  var womenDataset = parsed_data[1]

  $('#container').highcharts({
              chart: {type: 'bar'},
              title: {text: 'Bias Impact Simulation'},
              xAxis: {categories: ['1', '2', '3', '4', '5', '6', '7', '8'],
                      title: {text: null}},
              yAxis: {min: 0,
                      title: {text: '# of Employees',
                              align: 'high'},
                      labels: {overflow: 'justify'}
              },
              plotOptions: {
                  bar: {
                      dataLabels: {
                          enabled: true
                      }
                  }
              },
              legend: {
                  layout: 'vertical',
                  align: 'right',
                  verticalAlign: 'top',
                  x: -40,
                  y: 80,
                  floating: true,
                  borderWidth: 1,
                  backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
                  shadow: true
              },
              credits: {
                  enabled: false
              },
              series: [{
                  name: 'Men',
                  data: menDataset 
              }, {
                  name: 'Women',
                  data: womenDataset
              }]
          });
}

$.post("/bias", {bias: 10, gender: 'male'}, myFunc);


