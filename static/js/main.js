const chart1 = echarts.init(document.querySelector('#main'))
$(document).ready(() => {
    drawPM25chart()
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
                    tooltip: {},
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
                chart1.setOption(option);
            },
            error: () => alert('讀取失敗!'),
        }
    );
}