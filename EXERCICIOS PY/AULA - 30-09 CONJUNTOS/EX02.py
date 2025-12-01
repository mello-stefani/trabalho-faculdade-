#Demonstre como definir 2 conjuntos de números inteiros a seguir realizar as operações fundamentais abaixo.

#a. união entre conjuntos
#b. interseção entre conjuntos
#c. diferença entre conjuntos
#d. obter o tamanho do conjunto
#e. obter o valor máximo e mínimo do conjunto

conjunto_a = {1,2,3,4,5}
conjunto_b = {4,5,6,7,8}

uniao = conjunto_a.union(conjunto_b)
print("Resultado da união: ", uniao)


intersecao = conjunto_a.intersection(conjunto_b)
print("Resultado da interseção: ", intersecao)


diferenca = conjunto_a.difference(conjunto_b)
print("Resultado da diferença entre conjunto: ", diferenca)

tamanho_a = len(conjunto_a)
print("O tamanho A é :", tamanho_a)

tamanho_b = len(conjunto_b)
print("O tamanho B é: ", tamanho_b)



valorMax = max(conjunto_a)
print("O valor maximo de A é: ", valorMax)
valorMax = max(conjunto_b)
print("O valor maximo de B é: ", valorMax)

valorMin = min(conjunto_b)
print("O valor minimo de B é: ", valorMin)
valorMin = min(conjunto_a)
print("O valor minimo de A é: ", valorMin)









