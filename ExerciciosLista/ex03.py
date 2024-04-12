#Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

notas = []

for i in range(4):
    nota = float(input(f'Digite a nota [{i+1}]: '))
    notas.append(nota)

soma = sum(notas)
media = soma / len(notas)
print(f'A media das notas são: {media:.1f}')