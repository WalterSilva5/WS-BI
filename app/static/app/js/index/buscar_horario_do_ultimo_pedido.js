function buscar_horario_do_ultimo_pedido() {
    $.getJSON('https://localhost:8920/api/ultimo_pedido', function(dados) {
        if (dados !== null) {
            horario = (JSON.parse(JSON.stringify(Object.values(dados))))[0];
            $("#hora_do_ultimo_pedido").html(horario.slice(11, 19));
        } else {
            alert("OCORREU UM ERRO");
        }
    });
}

buscar_horario_do_ultimo_pedido();
setInterval(function() {
    buscar_horario_do_ultimo_pedido();
}, 120000);


/*<h6 class="text-info">HORA DO ULTIMO PEDIDO</h6>
        <h class="h3 font-weight-bold" id="hora_do_ultimo_pedido">00:00:00</h>*/