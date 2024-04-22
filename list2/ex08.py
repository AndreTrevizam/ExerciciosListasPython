#Conte quantas vezes o número 5 aparece na lista e imprima o resultado.

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_nova = list(range(5, 0, -1))

lista.extend(lista_nova)

count = 1

contagem = lista.count(5)
print("O número 5 aparece", contagem, "vezes na lista.")