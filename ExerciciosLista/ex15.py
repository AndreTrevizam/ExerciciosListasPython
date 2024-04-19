#Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
# Mostre a quantidade de valores que foram lidos;
# Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
# Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
# Calcule e mostre a soma dos valores;
# Calcule e mostre a média dos valores;
# Calcule e mostre a quantidade de valores acima da média calculada;
# Calcule e mostre a quantidade de valores abaixo de sete;
# Encerre o programa com uma mensagem;

notas_valores = []

while True:
    notas = float(input('Digite a nota: '))
    if notas < 0:
        break

    notas_valores.append(notas)

print(f'{len(notas_valores)} valores foram lidos')

for nota in notas_valores:
    print(nota, end=' ')
print()

for nota in reversed(notas_valores):
    print(nota)

soma = sum(notas_valores)
print(f'A soma total é: {soma}')

media = soma / len(notas_valores)
print(f'A media total é: {media}')

count = 0
for notas in notas_valores:
    if notas > media:
        count += 1
        print(f'Quantidade de valores acima da média calculada: {count}')

count_1 = 0
for notas in notas_valores:
    if notas < 7:
        count_1 += 1
        
if count_1 > 0:
    print(f'Existem {count_1} valores abaixo de 7')
else:
    print('Não existem valores abaixo de 7')