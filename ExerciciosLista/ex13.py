#Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

temperaturas_mes = []
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

for mes in meses:
    temp_media = float(input(f'Digite a temperatura media do mes {mes}: '))
    temperaturas_mes.append(temp_media)

media_anual = sum(temperaturas_mes) / len(temperaturas_mes)
print(f'A media anual é de {media_anual:.1f}°C')
print('-' * 20)

for i, temperatura in enumerate(temperaturas_mes):
    if temperatura > media_anual:
        print(f'{meses[i]}: {temperatura}°C')
