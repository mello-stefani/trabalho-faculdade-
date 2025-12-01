#1. Elabore uma aplicação em Python que implemente um jogo de Adivinhar o Número de 0 a 100 com as seguintes características:

#para geração do número oculto, utilizar a biblioteca Random
#o jogador terá um número de chances para acertar o número. Se não conseguir, a aplicação deverá mostrar qual era o número oculto
#a cada jogada, a aplicação deverá informar o número de tentativas restantes e se o número oculto é maior ou menor do o palpite do jogador


import random

print("Tente adivinhar o número secreto entre 0 e 100.\n")

# Gera o número secreto usando random
numero_secreto = random.randint(0, 100)

# Define o número máximo de tentativas
tentativas_totais = 5
tentativas_restantes = tentativas_totais

# Loop principal do jogo
while tentativas_restantes > 0:
    print(f"Tentativas restantes: {tentativas_restantes}")
    
    # Pede o palpite do jogador
    try:
        palpite = int(input("Digite seu palpite (0 a 100): "))
    except ValueError:
        print("Por favor, digite um número inteiro!\n")
        continue

    # Verifica se está dentro do intervalo válido
    if palpite < 0 or palpite > 100:
        print("O número deve estar entre 0 e 100!\n")
        continue

    # Verifica se acertou
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número {numero_secreto}!")
        break
    elif palpite < numero_secreto:
        print("O número secreto é MAIOR.\n")
    else:
        print("O número secreto é MENOR.\n")

    # Diminui o número de tentativas
    tentativas_restantes -= 1

# Se acabar as tentativas, revela o número
if tentativas_restantes == 0:
    print(f"ERRADO! O número secreto era {numero_secreto}.")
