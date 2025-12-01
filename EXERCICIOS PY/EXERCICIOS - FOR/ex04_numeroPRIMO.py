#(Desafio) Escreva um algoritmo que retorne os números primos existentes entre 1 e 1000.

print("Numeros primos entre 1 e 1000: ")

for i in range(2, 1001):
    primo = True
    for j in range(2,i):
        if(i % j == 0):
            primo = False
            break
        if (primo):
            print(i)

    

