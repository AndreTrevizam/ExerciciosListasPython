#Crie uma nova lista reversa dos números de 1 a 5 e adicione-a à lista original. Imprima a lista resultante.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_nova = list(range(5, 0, -1))

lista.extend(lista_nova)
print(lista)
    