#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

numeros = []
numeros_par = []
numeros_impar = []

#armazenar todos os numeros em uma array
for i in range(20):
    num = int(input(f'Digite um numero [{i+1}]: '))
    numeros.append(num)

    if num % 2 == 0:
        numeros_par.append(num)
    else:
        numeros_impar.append(num)

print('-' *20)
print(f'Todos os números: {numeros}')
print(f'Números pares: {numeros_par}')
print(f'Números impares: {numeros_impar}')