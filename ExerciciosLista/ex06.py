#Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

notas_alunos = []
count_alunos = 0

for i in range(10):
    soma = 0 #reiniciar a soma para cada aluno
    for j in range(4):
        nota = float(input(f'Digite a nota [{j+1}] do aluno [{i+1}]:'))
        soma += nota #adicionar a nota a soma do aluno
    media = soma / 4

    if media >= 7.0:
        count_alunos += 1

print(f'{count_alunos} com media maior ou igual a 7')
