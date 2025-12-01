//Desenvolva um algoritmo, que inclua 3 variáveis, 1º nome do
//aluno. 2º nota do aluno e 3º nota do trabalho do aluno. No final
//faça uma media. Verifique se o aluno ficou com nota, maior ou
//igual a 7. E mostre na tela se ele está ou não em exame


let aluno = {
    nome: "Eliezer",
    nota: 6,
    notaTrabalho: 5,
    soma: function() {
        return this.nota + this.notaTrabalho;
    },
    media: function(){
        return this.soma()/2
    },
    passou: function() {
        if (this.media() >=7) {
            console.log(this.nome + "Esta aprovado com média: " + this.media() + " e não precisará de exane.");
        } else {
            console.log(this.nome + " não está aprovado com média: " + this.media()+ " e precisará  de exame ");
        }
        }
    };
    aluno.passou(); 
