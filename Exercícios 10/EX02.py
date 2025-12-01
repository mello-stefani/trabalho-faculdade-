#Desenvolva uma aplicação que implemente o Jogo da Forca e que, a cada execução, escolha uma palavra aleatória de uma lista de palavras. O jogador poderá errar 5 vezes antes de ser "enforcado". A lista de palavras pode ser obtida de um arquivo ou Hard-coded. Abaixo, é sugerida uma interface no console para interação com o programa.


import random

def escolher_palavra():
    palavras = ['banana', 'cachorro', 'slipknot']
    return random.choice(palavras)

def jogar_forca():
    palavra = escolher_palavra()
    letras_corretas = []
    letras_erradas = []
    tentativas = 5

    while True:
        palavra_escondida = ''
        for letra in palavra:
            if letra in letras_corretas:
                palavra_escondida += letra
            else:
                palavra_escondida += '_'

        print("\nPalavra:", palavra_escondida)
        print("Letras erradas:", letras_erradas)
        print("Tentativas restantes:", tentativas)

        if '_' not in palavra_escondida:
            print("Parabéns! Você venceu!")
            break

        if tentativas == 0:
            print("Você perdeu! A palavra era:", palavra)
            break

        letra = input("Digite uma letra: ").lower()

        if letra in palavra:
            if letra not in letras_corretas:
                letras_corretas.append(letra)
        else:
            if letra not in letras_erradas:
                letras_erradas.append(letra)
                tentativas -= 1

jogar_forca()






    