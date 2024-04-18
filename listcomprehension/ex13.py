#Crie uma lista vazia e preencha-a com os números de 1 a 10 elevados ao quadrado usando uma estrutura de repetição.

lista = []

for i in range(1,11):
    i = i*i
    lista.append(i)

print(lista)