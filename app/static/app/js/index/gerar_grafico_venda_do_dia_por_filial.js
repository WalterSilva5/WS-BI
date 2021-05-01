function gera_grafico_venda_por_filial() {
    $.getJSON('http://localhost/api/api_vendas_do_dia_por_filial', function(dados) {
        if (dados !== null) {
            valor_venda_por_filial = [
                Array('FILIAL', 'VALOR'),
            ];
            valor_venda_por_filial.push(["MATRIZ", dados["filial1"]]);
            valor_venda_por_filial.push(["FILIAL", dados["filial2"]]);
            total = dados["filial1"] + dados["filial2"];

            function drawChart2() {
                var dat = google.visualization.arrayToDataTable(valor_venda_por_filial);

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
                    title: "Venda por filial",
                    width: 400,
                    height: 270,
                    bar: { groupWidth: "95%" },
                    legend: { position: "none" },
                };
                var chart = new google.visualization.ColumnChart(document.getElementById("grafico_vendas_por_filial"));
                chart.draw(view, options);
            }
            google.charts.load("current", { packages: ['corechart'] });
            google.charts.setOnLoadCallback(drawChart2);

            $("#total_vendas_por_filial").html("TOTAL: R$: " + total.toLocaleString('pt-br', { minimumFractionDigits: 2 }));

        } else {
            alert("OCORREU UM ERRO");
        }
    });
}
gera_grafico_venda_por_filial();

setInterval(function() {
    gera_grafico_venda_por_filial();
}, 120000);