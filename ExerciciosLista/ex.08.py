#Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.

alturas = []
idade = []

for i in range(5):
    idade_num = int(input(f'Digite a idade da pessoa [{i+1}]: '))
    idade.append(idade_num)
    altura_num = float(input(f'Digite a altura da pessoa [{i+1}] em metros: '))
    alturas.append(altura_num)

idade.reverse()
print(idade)

alturas.reverse()
print(alturas)