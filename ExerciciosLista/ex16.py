#Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#$200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
#ist in range

intervalos = [
    (200, 299),
    (300, 399),
    (400, 499),
    (500, 599),
    (600, 699),
    (700, 799),
    (800, 899),
    (900, 999),
    (1000, float('inf'))  # O último intervalo vai de 1000 em diante
]

# Inicialize uma lista de contadores para cada intervalo
contadores = [0] * len(intervalos)

num_vendedores = int(input('Digite o numero de vendedores: '))

for i in range(num_vendedores):
    vendas_brutas = float(input('Digite o valor das vendas brutas: '))
    salario_base = 200
    salario_total = salario_base + (vendas_brutas * 0.09)

for i, (intervalo_min, intervalo_max) in enumerate(intervalos): #i para o index. e intervalo_min por exemplo é o 200 e o intervalo_max é o 299
    if intervalo_min <= salario_total < intervalo_max:
        contadores[i] += 1
        break

for i, (intervalo_min, intervalo_max) in enumerate(intervalos):
    if intervalo_max == float('inf'):
        print(f'${intervalo_min} em diante: {contadores[i]} vendedores')
    else:
        print(f'${intervalo_min} - ${intervalo_max}: {contadores[i]} vendedores ')