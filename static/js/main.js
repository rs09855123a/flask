const chart1 = echarts.init(document.querySelector('#main'))
const chart2 = echarts.init(document.querySelector('#six'))
$(document).ready(() => {
    drawPM25chart();
    drawsixPM25chart()
})
function drawPM25chart() {
    $.ajax(
        {
            url: './pm25-data',
            type: 'POST',
            dataType: 'json',
            success: (data) => {
                console.log(data);
                var option = {
                    title: {
                        text: 'PM2.5全台資訊'
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'left',
                        top: 'center',
                        feature: {
                            magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                            restore: { show: true },
                            saveAsImage: { show: true }
                        }
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: data['PM2.5']
                    },
                    xAxis: {
                        data: data['site']
                    },
                    yAxis: {},
                    series: [
                        {
                            name: 'pm2.5',
                            type: 'bar',
                            data: data['pm25']
                        }
                    ]
                };
                document.querySelector('#pm25_high_site').innerText = data['highest'][0];
                document.querySelector('#pm25_high_value').innerText = data['highest'][1];
                $('#pm25_low_site').text(data['lowest'][0]);
                $('#pm25_low_value').text(data['lowest'][1]);
                $('#date').text(data['update_time']);
                chart1.setOption(option);
            },
            error: () => alert('讀取失敗!'),
        }
    );
}


function drawsixPM25chart() {
    $.ajax(
        {
            url: './six-pm25',
            type: 'POST',
            dataType: 'json',
            success: (data) => {
                console.log(data);
                var option = {
                    title: {
                        text: 'PM2.5六都平均值'
                    },
                    toolbox: {
                        show: true,
                        orient: 'vertical',
                        left: 'left',
                        top: 'center',
                        feature: {
                            magicType: { show: true, type: ['line', 'bar', 'tiled'] },
                            restore: { show: true },
                            saveAsImage: { show: true }
                        }
                    },
                    tooltip: {
                        trigger: 'axis'
                    },
                    legend: {
                        data: data['PM2.5']
                    },
                    xAxis: {
                        data: data['city']
                    },
                    yAxis: {},
                    series: [
                        {
                            name: 'pm2.5',
                            type: 'bar',
                            data: data['pm25']
                        }
                    ]
                };

                chart2.setOption(option);
            },
            error: () => alert('讀取失敗!'),
        }
    );
}