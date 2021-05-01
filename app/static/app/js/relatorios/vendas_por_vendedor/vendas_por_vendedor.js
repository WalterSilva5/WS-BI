$('#agrupar').change(function() {
    $('#buscar_vendas').click();
})

$('#data_final').blur(function() {
    $('#buscar_vendas').click();
})

function grafico_vendas_por_vendedor() {
    google.charts.load('current', { 'packages': ['corechart'] });
    google.charts.setOnLoadCallback(drawChart);
    mes = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julio", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ];

    function drawChart() {
        valores = $("#valores").val();
        valores = valores.split('[').join('');
        valores = valores.split(']').join('');
        valores = valores.split(',')
        ar_valores = [
            ['Ano', 'Vendas', ""],
        ];
        count = 0;
        for (x = 0; x < valores.length / 2; x++) {
            ar_valores.push([valores[count], parseFloat(valores[count + 1]), 0])
            count += 2
        }
        console.log(ar_valores);

        //valores = valores.slice(1, valores.length - 1).split("],");

        var data = google.visualization.arrayToDataTable(ar_valores);

        var options = {
            title: 'Vendas do RCA: ' + $("#codigorca").val() + ' por ' + $("#agrupamento").val(),
            curveType: 'function',
            width: 1200,
            height: 300,
            legend: { position: 'bottom' }
        };


        var chart = new google.visualization.LineChart(document.getElementById('grafico_venda_por_vendedor_por_periodo'));

        chart.draw(data, options);
    }
}
grafico_vendas_por_vendedor()