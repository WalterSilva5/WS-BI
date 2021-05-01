function gerar_grafico_venda_do_dia_por_vendedor() {
    $.getJSON('http://localhost/api/api_vendas_do_dia_por_vendedor', function(dados) {
        if (dados !== null) {
            data = (JSON.parse(JSON.stringify(Object.values(dados))))[0];
            teste = [
                Array('VENDEDOR', 'VALOR'),
            ];
            teste = teste.concat(data);
            valores = teste.slice(0, teste.length);
            total = 0;
            for (x = 1; x < teste.length; x++) {
                total += valores[x][1];
            }

            function drawChart() {
                var dat = google.visualization.arrayToDataTable(valores);

                var view = new google.visualization.DataView(dat);
                view.setColumns([0, 1,
                    {
                        calc: "stringify",
                        sourceColumn: 1,
                        type: "string",
                        role: "annotation"
                    },
                ]);

                var options = {
                    title: "VENDA DO DIA POR VENDEDOR",
                    height: 300,
                    bar: { groupWidth: "95%" },
                    legend: { position: "none" },
                };
                var chart = new google.visualization.ColumnChart(document.getElementById("grafico_de_vendas_por_vendedor"));
                chart.draw(view, options);
            }
            google.charts.load("current", { packages: ['corechart'] });
            google.charts.setOnLoadCallback(drawChart);
            $("#total_venda_do_dia_vendedores").html(" R$: " + total.toLocaleString('pt-br', { minimumFractionDigits: 2 }));

        } else {
            alert("OCORREU UM ERRO");
        }
    });

}
gerar_grafico_venda_do_dia_por_vendedor();
setInterval(function() {
    gerar_grafico_venda_do_dia_por_vendedor();
}, 120000);