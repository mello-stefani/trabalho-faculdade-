#Uma fábrica de camisetas produz os tamanhos pequeno, médio e grande, cada qual sendo vendido respectivamente por 10, 12 e 15 reais. Implemente um programa em que o usuário forneça a quantidade de camisetas pequenas, médias e grandes referentes a uma venda e retorne o valor a ser cobrado.

pequeno = 10
medio = 12 
grande = 15

camisaP = int(input("Quantidade de camisetas pequenas: "))
multiplicaP = pequeno*camisaP

camisaM = int(input("Quantidade de camisetas médias: "))
multiplicaM = medio*camisaM 

camisaG = int(input("Quantidade de camisetas grandes: "))
multiplicaG = grande*camisaG

print(f"Valor de camisetas P será de: R$ {multiplicaP}")
print(f"Valor de camisetas M será de: R$ {multiplicaM}")
print(f"Valor de camisetas G será de: R$ {multiplicaG}")
