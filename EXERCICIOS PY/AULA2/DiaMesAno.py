#Leia uma data informada pelo usuário (dia, mês e ano) e determine se aquela data é válida ou não

data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = map(int, data.split("/")) #split serve p dividir uma string em partes menores(listas)
bissexto = False

if ano <= 0 or ano > 3000:
  print("Ano inválido")
  

if ano % 4 == 0:
  bissexto = True

if bissexto:
  print("O ano é bissexto")
else:
  print("O ano não é bissexto")

if mes < 1 or mes > 12:
  print("Mês inválido")
  

if mes == 2: # fevereiro
  if bissexto:
    dias_no_mes = 29
  else:
    dias_no_mes = 28
elif mes in [4, 6, 9, 11]:
  dias_no_mes = 30
else:
  dias_no_mes = 31

if dia < 1 or dia > dias_no_mes:
  print("Dia inválido")

print("Data válida")