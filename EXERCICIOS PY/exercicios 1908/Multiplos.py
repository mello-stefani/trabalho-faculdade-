#Elaborar um algoritmo que lê 2 valores a e b, verifica se são múltiplos um do outro e os escreve com a mensagem: São múltiplos ou Não são múltiplos.

valor1 = int(input("Digite um valor: "))
valor2 = int(input("Digite outro valor: "))

if valor1 % valor2 == 0 or valor2 % valor1 == 0:
    print("São multiplos")

else:
    print("Não são multiplos")

