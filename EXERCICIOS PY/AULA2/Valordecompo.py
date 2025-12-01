#Ler um valor em reais e mostrar qual o número de notas de 100, 50, 20, 10, 5 e 2 em que o valor lido pode ser decomposto. Escrever o valor lido e a relação de notas necessárias.

valor = int(input("Digite o valor em reais: "))
resto = valor
notas_100 = 0
notas_50 = 0
notas_20 = 0
notas_10 = 0
notas_5 = 0
notas_2 = 0 

if resto >= 100:
    notas_100 = resto // 100
    resto = resto % 100
    
if resto >= 50:
    notas_50 = resto // 50
    resto = resto % 50
    
if resto >= 20:
    notas_20 = resto // 20
    resto = resto % 20

if resto >= 10:
    notas_10 = resto // 10
    resto = resto % 10

if resto >= 5:
    notas_5 = resto // 5
    resto = resto % 5

if resto >= 2:
    notas_2 = resto // 2
    resto = resto % 24

print(f"Valor: R$ {valor}")
print(f"{notas_100} nota(s) de R$ 100")
print(f"{notas_50} nota(s) de R$ 50")
print(f"{notas_20} nota(s) de R$ 20")
print(f"{notas_10} nota(s) de R$ 10")
print(f"{notas_5} nota(s) de R$ 5")
print(f"{notas_2} nota(s) de R$ 2")