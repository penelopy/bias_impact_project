var dataHasChanged = function(){
    bias = $("input[name=bias]:checked").val()
    gender = $("input[name=gender]:checked").val()
    $.post("/bias", {bias: bias, gender: gender}, renderGraph);
};

function renderGraph(data){
  // Grab data
  parsed_data = $.parseJSON(data);
  var menDataset = parsed_data[0];
  var womenDataset = parsed_data[1]

  // Render graph
  $('#container').highcharts({
    chart: {
        type: 'column'
    },
    title: {
        text: 'Gender Bias Simulator'
    },
    xAxis: {
        categories: [
            'Level 1',
            'Level 2',
            'Level 3',
            'Level 3',
            'Level 5',
            'Level 6',
            'Level 7',
            'Level 8'
        ],
        crosshair: true
    },
    yAxis: {
        min: 0,
        title: {
            text: 'Percentage'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f} %</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    },
    plotOptions: {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
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

$.post("/bias", {bias: 10, gender: 'male'}, renderGraph);
