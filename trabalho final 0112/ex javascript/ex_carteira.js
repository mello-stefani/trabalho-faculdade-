function verificaIdade() {
    let idade = document.getElementById('idade'). value;
 
    let resultado = document.getElementById('resultado'); 

    if (idade >= 21) {
	resultado.innerHTML = "Você pode fazer a carteira de motorista do tipo AB e D.";
    } else if (idade >= 18) {
   	resultado.innerHTML = "Você pode fazer a carteira de motorista do tipo AB."; 
    } else {
	resultado.innerHTML = "Você não tem idade para fazer a carteira de motorista.";
    }
};