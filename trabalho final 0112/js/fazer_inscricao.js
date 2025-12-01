document.addEventListener("DOMContentLoaded", function() {
    const eventos = {
        1: { nome: "A casa que susurra", descricao: "O que é real e o que não é?", vagas: 15, valor: 50 },
        2: { nome: "A Noite da Caçada", descricao: "O escuro não dorme.", vagas: 5, valor: 80 },
        3: { nome: "Ele sempre sabe onde você está", descricao: "Encontro de contos.", vagas: 0, valor: 100 },
        4: { nome: "O Grito Final", descricao: "LENDAS.", vagas: 25, valor: 60 },
    };

    const selectEvento = document.getElementById("select_evento");
    const containerFormulario = document.getElementById("container_formulario");
    const form = document.getElementById("formulario_inscricao");

    const infoDiv = document.createElement("div");
    infoDiv.classList.add("alert", "mt-3");
    containerFormulario.appendChild(infoDiv); 

    

    selectEvento.addEventListener("change", function() {
        const eventoSelecionado = eventos[this.value];

        if (!eventoSelecionado) return;

        let classeAlerta = eventoSelecionado.vagas > 0 ? "alert-success" : "alert-danger";
        infoDiv.className = `alert ${classeAlerta} mt-3`;

        infoDiv.innerHTML = `
            <strong>${eventoSelecionado.nome}</strong><br>
            ${eventoSelecionado.descricao}<br>
            Vagas disponíveis: <b>${eventoSelecionado.vagas}</b><br>
            Valor da inscrição: <b>R$ ${eventoSelecionado.valor.toFixed(2)}</b>
        `;
    });

    form.addEventListener("submit", function(e) {
        e.preventDefault();
        const eventoId = selectEvento.value;

        if (!eventoId) {
            alert("Selecione um evento antes de prosseguir!");
            return;
        }

        const evento = eventos[eventoId];
        if (evento.vagas === 0) {
            alert("SEM INGRESSOS DISPONÍVEIS! NOS VEMOS NA PRÓXIMA");
            return;
        }

        infoDiv.className = "alert alert-info mt-3";
        infoDiv.innerHTML = `
            ✅Bem-vindos ao horror!<br>
            <b>${evento.nome}</b> - Valor: R$ ${evento.valor.toFixed(2)}<br>
            Um e-mail perturbador aparecerá na sua caixa de entrada.
        `;
    });
});
