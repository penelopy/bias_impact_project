$(function () {
    $("button").on("click", function() {
    bias = event.target.dataset.bias;

    $.post("/bias", {bias: bias}, function(data, success) {
        parsed_data = $.parseJSON(data);
        var menDataset = parsed_data[0];
        var womenDataset = parsed_data[1]

        $('#container').highcharts({
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Bias Impact Simulation'
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
                    text: '# of Employees',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                }
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
                // $({{ male_json|tojson }}) //
                // data: [9.01, 29.12, 38.71, 48.66, 72.49, 97.75, 169.88, 247.58]
            }, {
                name: 'Women',
                data: womenDataset
                // $({{ female_json|tojson }}) //
                // data: [.99, 10.88, 36.29, 51.34, 77.51, 102.25, 180.12, 252.42]
            }]
        });

    });
    });
});


$.post("/bias", {bias: 10}, function(data, success) {
    parsed_data = $.parseJSON(data);
    var menDataset = parsed_data[0];
    var womenDataset = parsed_data[1]

$('#container').highcharts({
            chart: {
                type: 'bar'
            },
            title: {
                text: 'Bias Impact Simulation'
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
                    text: '# of Employees',
                    align: 'high'
                },
                labels: {
                    overflow: 'justify'
                }
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
                // $({{ male_json|tojson }}) //
                // data: [9.01, 29.12, 38.71, 48.66, 72.49, 97.75, 169.88, 247.58]
            }, {
                name: 'Women',
                data: womenDataset
                // $({{ female_json|tojson }}) //
                // data: [.99, 10.88, 36.29, 51.34, 77.51, 102.25, 180.12, 252.42]
            }]
        });

    });


