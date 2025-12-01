# Elabore um programa que implementa o Jogo da Velha utilizando uma matriz de elementos 3 x 3 para armazenar as jogadas. Abaixo, é sugerida uma interface no console para interação com o programa



#mostra tabuleiro
def mostrar_tabuleiro(tabuleiro):
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()

# Função para checar vitória
def checar_vitoria(tabuleiro, jogador):
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    for c in combinacoes:
        if tabuleiro[c[0]] == tabuleiro[c[1]] == tabuleiro[c[2]] == jogador:
            return True
    return False

#Função
def jogo_da_velha():
    tabuleiro = [" "]*9
    jogador_atual = "X"

    for turno in range(9):
        mostrar_tabuleiro(tabuleiro)
        try:
            jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if tabuleiro[jogada] != " ":
                print("Posição já ocupada! Tente novamente.")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Escolha um número de 1 a 9.")
            continue

        tabuleiro[jogada] = jogador_atual

        if checar_vitoria(tabuleiro, jogador_atual):
            mostrar_tabuleiro(tabuleiro)
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            return

        jogador_atual = "O" if jogador_atual == "X" else "X"

    mostrar_tabuleiro(tabuleiro)
    print("Empate!")

# Executa o jogo
jogo_da_velha()


#fiz essa com ajuda do chaat :(

