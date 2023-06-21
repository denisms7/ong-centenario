window.onload = function() {
    adicionarClasseAtiva();
};

function adicionarClasseAtiva() {
    var elementos = document.getElementsByClassName('botoes_ativos');

    for (var i = 0; i < elementos.length; i++) {
        elementos[i].addEventListener('click', function () {
            // Remove a classe 'active' de todos os elementos
            for (var j = 0; j < elementos.length; j++) {
                elementos[j].classList.remove('active');
            }

            // Adiciona a classe 'active' ao elemento clicado
            this.classList.add('active');
        });
    }
}
