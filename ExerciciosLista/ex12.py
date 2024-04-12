#foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

idades = []
alturas = []

for i in range(30): 
    idade = int(input(f'Digite a idade [{i+1}]: '))
    idades.append(idade)
    altura = float(input(f'Digite a altura [{i+1}] em metros: '))
    alturas.append(altura)

soma_alturas = sum(alturas)
media_altura = soma_alturas / 30
quant_alunos = 0

for j in range(30):
    if idades[j] > 13 and alturas[j] < media_altura:
        quant_alunos += 1

print(f'A quantidade de alunos com mais de 13 anos que possuem altura inferior a media de altura são: [{quant_alunos}]')