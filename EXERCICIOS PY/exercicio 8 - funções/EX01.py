#1. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato 
# DD de MÊS de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def data(ddmmyyyy):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio",
             "junho", "julho", "agosto", "setembro", "outubro",
             "novembro", "dezembro"]
    dd = int(ddmmyyyy[:2])
    mm = int(ddmmyyyy[3:5])
    yyyy = int(ddmmyyyy[6:10])
    return dd + " de " + meses[mm] + " de " + yyyy

#NAO ENTENDIII


