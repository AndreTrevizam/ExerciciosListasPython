#Dada uma lista de nomes, crie uma nova lista contendo apenas os nomes que começam com a letra 'A'.

lista = ['andre', 'macarrao', 'caminhao', 'macaco', 'agua', 'anderson']

lista_nova = [nome for nome in lista if nome.startswith('a')]

print(lista_nova)