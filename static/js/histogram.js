var dataHasChanged = function(){
    renderGraphTemplate();
    bias = $("input[name=bias]:checked").val()
    gender = $("input[name=gender]:checked").val()
    $.post("/bias", {bias: bias, gender: gender}, renderGraph);
};


function mattTest(){
    console.log('test');
}

function renderGraph(data){
  // Grab data
  parsed_data = $.parseJSON(data);
  var menDataset = parsed_data[0];
  var womenDataset = parsed_data[1];
  var bias_amount = parsed_data[2];
  var gender_favored = parsed_data[3]

  // Render graph
  $('#container').highcharts({
    chart: {
        type: 'column'
    },
    title: {
        text: 'Promotion Bias Simulator'
    },
    labels: {
        items: [{
            html: 'Graph displays a {{ bias_amount }} bias in favor of {{ gender_favored }}',
            style: {
                left: '50px',
                top: '18px',
                color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
            }
        }]
    },
    xAxis: {
        categories: [
            'Level 1: Entry Level',
            'Level 2',
            'Level 3',
            'Level 4',
            'Level 5',
            'Level 6',
            'Level 7',
            'Level 8: Exec Level'
        ],
        // crosshair: true
    },
    yAxis: {
        min: 0,
        max: 100,
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
        name: 'Women',
        data: womenDataset, 
        color: '#B1D3ED'
    }, {name: 'Men',
        data: menDataset, 
        color: '#346F9A'
    }]
  });
}

function renderGraphTemplate(data){
// Render empty graph
  $('#container').highcharts({
    chart: {
        type: 'column'
    },
    title: {
        text: 'Promotion Bias Simulator'
    },
    labels: {
            items: [{
                html: 'Graph displays a x bias in favor of MEN',
                style: {
                    left: '50px',
                    top: '18px',
                    color: (Highcharts.theme && Highcharts.theme.textColor) || 'black'
                }
            }]
        },
    xAxis: {
        categories: [
            'Level 1',
            'Level 2',
            'Level 3',
            'Level 4',
            'Level 5',
            'Level 6',
            'Level 7',
            'Level 8'
        ],
        // crosshair: true
    },
    yAxis: {
        min: 0,
        max: 100,
        title: {
            text: 'Percentage'
        },
        categories: [
            'Women', 
            'Men'
        ],
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
        data: [0,0,0,0,0,0,0,0]
    }, {
        name: 'Women',
        data: [0,0,0,0,0,0,0,0]
        }]
  });
}

$.post("/bias", {bias: 10, gender: 'male'}, renderGraph);

