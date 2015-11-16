

$(function () {
    $('#container').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: 'Bias Impact Simulation'
        },
        subtitle: {
            text: 'Source: <a href="http://www.ruf.rice.edu/~lane/papers/male_female.pdf"</a>'
        },
        xAxis: {
            categories: ['1', '2', '3', '4', '5', '6', '7', '8'],
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Percentage',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        tooltip: {
            valueSuffix: ' millions'
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
            data: [9.01, 29.12, 38.71, 48.66, 72.49, 97.75, 169.88, 247.58]
        }, {
            name: 'Women',
            data: [.99, 10.88, 36.29, 51.34, 77.51, 102.25, 180.12, 252.42]
        }]
    });
});