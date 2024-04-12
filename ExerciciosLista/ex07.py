#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

lista = []
produto = 1

for i in range(5):
    num = int(input(f'Digite o numero [{i+1}]: '))
    lista.append(num)

soma = sum(lista)
print(soma)

for numero in lista:
    produto *= numero
print(produto)

print(lista)