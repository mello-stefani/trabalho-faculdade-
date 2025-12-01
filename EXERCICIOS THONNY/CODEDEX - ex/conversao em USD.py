# solicite ao usuário o valor que ele tem em pesos, soles e reais e calcule o total em USD.

pesos = float(input('Quanto você tem em pesos colombianos? '))
soles = float(input('Quanto você tem em soles peruanos? '))
reais = float(input('Quanto você tem em reais? ')) 

total = pesos * 0.00026 + soles * 0.29 + reais * 0.19

print(total)