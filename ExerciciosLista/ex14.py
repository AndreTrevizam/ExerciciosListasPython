#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

respostas = []

# pergunta_1 = input('Telefonou para a vitima? (sim ou nao): ')
# respostas.append(pergunta_1)
# pergunta_2 = input('Esteve no local do crime? (sim ou nao): ')
# respostas.append(pergunta_2)
# pergunta_3 = input('Mora perto da vitima? (sim ou nao): ')
# respostas.append(pergunta_3)
# pergunta_4 = input('Devia para a vitima? (sim ou nao): ')
# respostas.append(pergunta_4)
# pergunta_5 = input('Ja trabalhou com a vitima? (sim ou nao): ')
# respostas.append(pergunta_5)

perguntas = [
    "Telefonou para a vítima? (sim ou não): ",
    "Esteve no local do crime? (sim ou não): ",
    "Mora perto da vítima? (sim ou não): ",
    "Devia para a vítima? (sim ou não): ",
    "Já trabalhou com a vítima? (sim ou não): "
]

for pergunta in perguntas:
    resposta = input(pergunta)
    respostas.append(resposta.lower())

contador = respostas.count('sim')

if contador == 2:
    print('Suspeita')
elif contador >= 2 and contador <= 4:
    print('Cumplice')
elif contador == 5:
    print('Assassino')
else:
    print('Inocente')