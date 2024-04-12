#Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

caracteres = [] #lista para armazenar os caracteres
consoantes = [] #lista para armazenar as consoantes
vogais = ['a', 'e', 'i', 'o', 'u']
consoantes_lidas = 0

for i in range(10):
    caractere = input(f'Digite um caractere[{i+1}]: ')
    caracteres.append(caractere)

for caractere in caracteres:
    if caractere not in vogais:
        consoantes_lidas += 1
        consoantes.append(caractere)

print(f'O total de consoantes lidas foram: {consoantes}')