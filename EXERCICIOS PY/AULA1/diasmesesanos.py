# Leia um número correspondendo a uma quantidade de dias e após, calcule e mostre a quantidade de anos, meses e dias correspondentes. Para facilitar o cálculo, considere ano com 365 dias e mês com 30 dias.
#ex.: 400 equivale a 1 ano, 1 mês e 5 dias

dias = int(input("Digite a quantidade de dias: "))


if dias >= 365: 
    qtdAnos = dias // 365
    dias = dias - (365 * qtdAnos)
    print("Quantidade de anos", qtdAnos)
if dias >= 30: 
    qtdMes = dias // 30
    dias = dias - (30 * qtdMes)
    print("Quantidade de meses", qtdMes)


print("Quantidade de dias", dias)

