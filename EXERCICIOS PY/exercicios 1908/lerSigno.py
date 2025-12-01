#Desenvolva um algoritmo que leia o nome de uma pessoa, o dia e o mês de seu nascimento e sem seguida apresente o nome da pessoa e o seu signo

dia = int(input("Informe o dia do seu nascimento [1-31]: "))
mes = int(input("Informe o mes do seu nascimento [1-12]: "))
nome = input("Informe seu nome: ")

#conversao da data
mesDia = (mes*100) + dia



#classifiqu signo 

if mesDia >= 21 and mesDia <= 218: 
    signo = "aquario"

elif mesDia >= 219 and mesDia <= 320:
    signo = "peixes"

elif mesDia >= 321 and mesDia <= 420:
    signo = "aries"

elif mesDia >= 421 and mesDia <= 521:
    signo = "touro"

elif mesDia >= 522 and mesDia <= 621:
    signo = "gemeos"

elif mesDia >= 622 and mesDia <= 722:
    signo = "cancer"

elif mesDia >= 723 and mesDia <= 823:
    signo = "leao" 

elif mesDia >= 824 and mesDia <= 922:
    signo = "virgem"

elif mesDia >= 923 and mesDia <= 1023:
    signo = "libra" 

elif mesDia >= 1024 and mesDia <= 1122:
    signo = "escorpiao"

elif mesDia >= 1123 and mesDia <= 1123:
    signo = "sagitario"

elif mesDia >= 1222 and mesDia <= 1231:
    signo = "capricornio"

elif mesDia >= 101 and mesDia <= 131:
    signo = "capricornio"

print(f"Olá {nome}, você é do signo de {signo}")