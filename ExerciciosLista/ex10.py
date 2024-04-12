#Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

vetor_a = [1,2,3,4,5,6,7,8,9,10]
vetor_b = [11,12,13,14,15,16,17,18,19,20]
vetor_c = []

for i in range(10):
    vetor_c.append(vetor_a[i])
    vetor_c.append(vetor_b[i])

print(vetor_c)