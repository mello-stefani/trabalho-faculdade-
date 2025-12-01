#Leia duas listas com 10 elementos cada. Gere um terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outras listas. 
 
lista1 = ["banana", "laranja", "maça", "limão", "pera", "arroz", "feijão", "macarrao", "mandioca", "uva"]
lista2 = ["cenoura", "bergamota", "manga", "tomate", "presunto", "queijo", "alface", "repolho", "beterraba", "pepino"]

lista3 = []

for i in range(10):  # como cada lista tem 10 elementos
    lista3.append(lista1[i]) #adiciona
    lista3.append(lista2[i])

print(lista3)
