#5. Escreva uma função Python que recebe um vetor de inteiros de qualquer tamanho e informe se os elementos do array estão classificados em ordem crescente, ou seja, ordenados do menor para o maior. A função deverá retornar um valor true ou false.

def crescente(vetor):
    ordenado = True
    for i in range(len(vetor) - 1):
        if vetor[i] > vetor[i + 1]:
            ordenado = False
            break
    return ordenado

numeros = [1, 2, 3, 4, 5]

resultado = crescente(numeros)

print(resultado)