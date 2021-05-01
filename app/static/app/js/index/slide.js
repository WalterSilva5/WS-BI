function slide(id) {
    function deslisar() {
        atual += 1;
        $(id).scrollTop(atual);
        if (atual > $(id).scrollTop()) {
            $(id).scrollTop(0);
            atual = 0;
        }
    }
    atual = 0;
    setInterval(function() {
        deslisar(atual);
    }, 300);
}

slide("#slide_produtos");
slide("#slide_metas");