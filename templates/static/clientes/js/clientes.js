function add_carro() {
    var container = document.getElementById("form-carro");

    var html = `
        <br>
        <div class="row">
            <div class="col-md">
                <input type="text" placeholder="Moto" class="form-control" name="carro">
            </div>
            <div class="col-md">
                <input type="text" placeholder="Placa" class="form-control" name="placa">
            </div>
            <div class="col-md">
                <input type="number" placeholder="Ano" class="form-control" name="ano">
            </div>
        </div>
    `;

    container.innerHTML += html;
}

function exibir_form(tipo) {
    add_cliente = document.getElementById('adicionar-cliente')
    att_cliente = document.getElementById('att_cliente')

    if(tipo == "1") {
        att_cliente.style.display = "none"
        add_cliente.style.display = "block"
    }else if(tipo == "2") {
        att_cliente.style.display = "block"
        add_cliente.style.display = "none"
    }
}