
// FORMATAR TELEFONE
function mascaraFone0(event) {
    var valor = document.getElementById("id_fone_1").attributes[0].ownerElement['value'];
    var retorno = valor.replace(/\D/g, "");
    retorno = retorno.replace(/^0/, "");
    if (retorno.length > 10) {
        retorno = retorno.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (retorno.length > 5) {
        if (retorno.length == 6 && event.code == "Backspace") {
            // necessário pois senão o "-" fica sempre voltando ao dar backspace
            return;
        }
        retorno = retorno.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (retorno.length > 2) {
        retorno = retorno.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        if (retorno.length != 0) {
            retorno = retorno.replace(/^(\d*)/, "($1");
        }
    }
    document.getElementById("id_fone_1").attributes[0].ownerElement['value'] = retorno;
}

function mascaraFone1(event) {
    var valor = document.getElementById("telefone1").attributes[0].ownerElement['value'];
    var retorno = valor.replace(/\D/g, "");
    retorno = retorno.replace(/^0/, "");
    if (retorno.length > 10) {
        retorno = retorno.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (retorno.length > 5) {
        if (retorno.length == 6 && event.code == "Backspace") {
            // necessário pois senão o "-" fica sempre voltando ao dar backspace
            return;
        }
        retorno = retorno.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (retorno.length > 2) {
        retorno = retorno.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        if (retorno.length != 0) {
            retorno = retorno.replace(/^(\d*)/, "($1");
        }
    }
    document.getElementById("telefone1").attributes[0].ownerElement['value'] = retorno;
}

function mascaraFone2(event) {
    var valor = document.getElementById("telefone2").attributes[0].ownerElement['value'];
    var retorno = valor.replace(/\D/g, "");
    retorno = retorno.replace(/^0/, "");
    if (retorno.length > 10) {
        retorno = retorno.replace(/^(\d\d)(\d{5})(\d{4}).*/, "($1) $2-$3");
    } else if (retorno.length > 5) {
        if (retorno.length == 6 && event.code == "Backspace") {
            // necessário pois senão o "-" fica sempre voltando ao dar backspace
            return;
        }
        retorno = retorno.replace(/^(\d\d)(\d{4})(\d{0,4}).*/, "($1) $2-$3");
    } else if (retorno.length > 2) {
        retorno = retorno.replace(/^(\d\d)(\d{0,5})/, "($1) $2");
    } else {
        if (retorno.length != 0) {
            retorno = retorno.replace(/^(\d*)/, "($1");
        }
    }
    document.getElementById("telefone2").attributes[0].ownerElement['value'] = retorno;
}


// CEP

// Fonte: https://viacep.com.br/exemplo/javascript/
function limpa_formulário_cep() {
    //Limpa valores do formulário de cep.
    document.getElementById('id_endereco').value = ("");
    document.getElementById('id_bairro').value = ("");
    document.getElementById('id_cidade').value = ("");
    document.getElementById('id_estado').value = ("");
}


function meu_callback(conteudo) {
    const divCep = document.getElementById('ceplog')
    if (!("erro" in conteudo)) {
        //Atualiza os campos com os valores.
        document.getElementById('id_endereco').value = (conteudo.logradouro);
        document.getElementById('id_bairro').value = (conteudo.bairro);
        document.getElementById('id_cidade').value = (conteudo.localidade);
        document.getElementById('id_estado').value = (conteudo.uf);
    } //end if.
    else {
        //CEP não Encontrado.
        limpa_formulário_cep();
        // alert("CEP não encontrado.");

        divCep.classList.add("show");
        divCep.classList.remove("d-none");
        divCep.classList.add("d-block");


    }
}

function pesquisacep(valor) {
    const divCep = document.getElementById('ceplog')
    const lupaCep = document.getElementById('lupacep')
    const spinnerCep = document.getElementById('spinnercep')
    lupaCep.classList.add("d-none");
    spinnerCep.classList.remove("d-none");

    //Nova variável "cep" somente com dígitos.
    var cep = valor.replace(/\D/g, '');

    //Verifica se campo cep possui valor informado.
    if (cep != "") {

        //Expressão regular para validar o CEP.
        var validacep = /^[0-9]{8}$/;

        //Valida o formato do CEP.
        if (validacep.test(cep)) {

            //Preenche os campos com "..." enquanto consulta webservice.
            document.getElementById('id_endereco').value = "...";
            document.getElementById('bairro').value = "...";
            document.getElementById('cidade').value = "...";
            document.getElementById('id_estado').value = "...";

            //Cria um elemento javascript.
            var script = document.createElement('script');

            //Sincroniza com o callback.
            script.src = 'https://viacep.com.br/ws/' + cep + '/json/?callback=meu_callback';

            //Insere script no documento e carrega o conteúdo.
            document.body.appendChild(script);

            // Remove aviso
            divCep.classList.remove("show");
            divCep.classList.add("d-none");
            divCep.classList.remove("d-block");


        } //end if.
        else {
            //cep é inválido.
            limpa_formulário_cep();
            // alert("Formato de CEP inválido.");

            divCep.classList.add("show");
            divCep.classList.remove("d-none");
            divCep.classList.add("d-block");

        }
    } //end if.
    else {
        //cep sem valor, limpa formulário.
        limpa_formulário_cep();
        divCep.classList.remove("show");
        divCep.classList.add("d-none");
        divCep.classList.remove("d-block");
    }

    lupaCep.classList.remove("d-none");
    spinnerCep.classList.add("d-none");

};

function TestaCPF(strCPF) {

    var Soma;
    var Resto;
    Soma = 0;
    if (strCPF == "00000000000") return false;
    if (strCPF == "11111111111") return false;
    if (strCPF == "22222222222") return false;
    if (strCPF == "33333333333") return false;
    if (strCPF == "44444444444") return false;
    if (strCPF == "55555555555") return false;
    if (strCPF == "66666666666") return false;
    if (strCPF == "77777777777") return false;
    if (strCPF == "88888888888") return false;
    if (strCPF == "99999999999") return false;

    for (i = 1; i <= 9; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (11 - i);
    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(9, 10))) return false;

    Soma = 0;
    for (i = 1; i <= 10; i++) Soma = Soma + parseInt(strCPF.substring(i - 1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;

    if ((Resto == 10) || (Resto == 11)) Resto = 0;
    if (Resto != parseInt(strCPF.substring(10, 11))) return false;
    return true;
}


function ValidaCPF() {
    let formCpf = document.getElementById('cpf')
    const cpflog = document.getElementById('cpflog')
    teste = TestaCPF(formCpf.value)

    if (formCpf.value.length == 0) {
        teste = true
    }

    if (teste) {
        cpflog.classList.add("d-none");
        cpflog.classList.remove("d-block");
    } else {
        cpflog.classList.remove("d-none");
        cpflog.classList.add("d-block");
    }

}


function AbrirConjuge() {
    const divConjuge = document.getElementById('div_conjuge')
    let estadoCivil = document.getElementById('estado_civil').value
    teste = false

    if (estadoCivil == 1) {
        teste = true
    } 
    if (estadoCivil == 3) {
        teste = true
    } 


    if (teste) {
        divConjuge.classList.add("show");
    }
    else {
        divConjuge.classList.remove("show");
        document.getElementById('conjuge_nome').value = ''
        document.getElementById('conjuge_sobrenome').value = ''
    }
}

function ColorirStatus() {
    let Campo = document.getElementById(id_status)

    if (Campo.value() == 1 ) {
        Campo.style.color = "#008000"
    }

    console.log(Campo.value())
}

function teste() {
    alert("Eu sou um alert!");
}
