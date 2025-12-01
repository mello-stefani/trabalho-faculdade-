idade = int(input("Informe sua idade: "))

if idade >= 18:   # > sinal maior
    print("Maior de idade: ")
else: 
    print("Menor de idade")
  
#-------# 

if idade >= 50: 
    print("Senior")
elif idade >= 21:
    print("Pleno")
elif idade >= 18:
    print("Junior")
else: 
    print("Iniciante")