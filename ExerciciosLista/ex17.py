#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
# Atleta: Rodrigo Curvêllo
 
# Primeiro Salto: 6.5 m
# Segundo Salto: 6.1 m
# Terceiro Salto: 6.2 m
# Quarto Salto: 5.4 m
# Quinto Salto: 5.3 m

# Resultado final:
# Atleta: Rodrigo Curvêllo
# Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
# Média dos saltos: 5.9 m
while True:
    nome_atleta = input('Digite o nome do atleta: ')

    if nome_atleta == '':
        break
        
    saltos = []

    for i in range(5):
        saltos_valores = float(input('Digite a distancia do salto (em metros): '))
        saltos.append(saltos_valores)

    media_saltos = sum(saltos) / len(saltos)

    print(f'Atleta: {nome_atleta}\n')

    for i, salto in enumerate(saltos, start=1):
        print(f'{i}º Salto: {salto} m')
    print(f'\nResultado final:\nAtleta: {nome_atleta}\nSaltos: {' - '.join(map(str, saltos))}\nMédia dos saltos: {media_saltos:.1f} m')