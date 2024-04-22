#Dada uma lista de números, crie uma nova lista contendo apenas os números pares da lista original.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_nova = [numeros for numeros in lista if numeros % 2 == 0]

print(lista_nova)