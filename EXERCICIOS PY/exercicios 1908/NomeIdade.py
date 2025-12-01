#leia o nome e a idade de três pessoas e após a leitura escreva o nome da pessoa mais velha e o nome da pessoa mais nova

# Leitura de nomes e idades
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a idade da primeira pessoa: "))

nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))

nome3 = input("Digite o nome da terceira pessoa: ")
idade3 = int(input("Digite a idade da terceira pessoa: "))

# Descobrindo a pessoa mais velha
if idade1 >= idade2 and idade1 >= idade3:
    maisVelha = nome1
elif idade2 >= idade1 and idade2 >= idade3:
    maisVelha = nome2
else:
    maisVelha = nome3

# Descobrindo a pessoa mais nova
if idade1 <= idade2 and idade1 <= idade3:
    maisNova = nome1
elif idade2 <= idade1 and idade2 <= idade3:
    maisNova = nome2
else:
    maisNova = nome3

print(f"A pessoa mais velha é: {maisVelha}")
print(f"A pessoa mais nova é: {maisNova}")
