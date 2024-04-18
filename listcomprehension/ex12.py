#Dada uma lista de strings, crie uma nova lista contendo apenas as strings com mais de 5 caracteres.

lista = ['andre', 'macarrao', 'caminhao', 'macaco', 'agua']

string_maior_que_5 = [palavras for palavras in lista if len(palavras) > 5]

print(string_maior_que_5)