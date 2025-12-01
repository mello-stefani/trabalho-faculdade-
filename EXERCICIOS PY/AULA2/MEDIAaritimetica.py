#3. Leia 3 notas de um aluno e em seguida calcule a média aritmética e mostre, além do valor da média, uma mensagem de "APROVADO", caso a média seja igual ou superior a 7, ou a mensagem "REPROVADO", caso contrário.

nota1 = float(input("Digite a nota: "))
nota2 = float(input("Digite a nota: "))
nota3 = float(input("Digite a nota: "))



media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("APROVADO")
else:
    media < 7
    print("REPROVADO")