let overviewChart;
let globalChartType = 'line';
let labels = [];
for (i = 0; i < overviewChartData.length; i++) { labels.push(i); }
let overviewChartJsData = {
    labels: labels,
    datasets: [{
        label: 'Sentimental Progress',
        data: overviewChartData,
        backgroundColor: 'rgba(75, 94, 178, 0.5)',
        borderColor: 'rgba(75, 94, 178, 1)',
        borderWidth: 1,
        fill: true
    }]
};
let options = {
    scales: {
        xAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Days'
                }
            }],
        yAxes: [{
            scaleLabel: {
                display: true,
                labelString: 'Progress %'
            },
            ticks: {
                callback: function (value, index, values) {
                    return value + '%';
                }
            }
        }]
    }
};

function updateZoom() {
    labels = [];
    const zoom = document.getElementById('graph-zoom').value;
    document.getElementById('graph-zoom-label').innerHTML = 'Graph Zoom Factor: ' + zoom;
    for (i = zoom; i < overviewChartData.length; i++) { labels.push(i); }
    if (overviewChart != undefined) {
        overviewChart.destroy();
        overviewChartJsData.labels = labels;
        overviewChartJsData.datasets[0].data = overviewChartData.slice(zoom);
    }
    overviewChart = new Chart(document.getElementById('overview-chart-ctx').getContext('2d'), {
        type: globalChartType,
        data: overviewChartJsData,
        options: options
    });
}

function changeChartType(chartType) {
    if (chartType == 'line') { document.getElementById('bar').classList.remove('active'); }
    else if (chartType == 'bar') { document.getElementById('line').classList.remove('active'); }
    document.getElementById(chartType).classList.add('active');
    if (overviewChart != undefined) { overviewChart.destroy(); }
    overviewChart = new Chart(document.getElementById('overview-chart-ctx').getContext('2d'), {
        type: chartType,
        data: overviewChartJsData,
        options: options
    });
    globalChartType = chartType;
}

changeChartType('line');
