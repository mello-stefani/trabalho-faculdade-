#Desenvolva um algoritmo que leia números até que a soma destes números seja maior do que 100. Ao final, o algoritmo deverá exibir quantos números foram lidos até que a condição de parada fosse atingida.

soma = 0
lidos = 0

while soma <= 100:  # continua até a soma ultrapassar 100
    numero = int(input("Informe um número: "))
    soma += numero
    lidos += 1

print(f"A soma final foi {soma}")
print(f"Foram lidos {lidos} números até ultrapassar 100")

