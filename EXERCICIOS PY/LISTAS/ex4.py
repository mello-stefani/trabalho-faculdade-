#Leia as quatro notas de 10 alunos, calcule e armazene em uma lista a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias = []  #armazena a média de cada aluno

for i in range(10):  # 10 alunos
    soma_notas = 0
    for j in range(4):  # 4 notas por aluno
        nota = float(input(f"Digite a {j+1}ª nota do aluno {i+1}: "))
        soma_notas += nota
    
    media = soma_notas / 4
    medias.append(media)

#quantos tiveram média >= 7
aprovados = 0
for m in medias:
    if m >= 7.0:
        aprovados += 1

print(f"O número de alunos com média maior ou igual a 7.0 é {aprovados}")

