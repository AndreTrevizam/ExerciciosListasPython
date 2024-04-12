#Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor_a = [1,2,3,4,5,6,7,8,9,10]
vetor_b = [11,12,13,14,15,16,17,18,19,20]
vetor_c = [21,22,23,24,25,26,27,28,29,30]
vetor_d = []

for i in range(10):
    vetor_d.append(vetor_a[i])
    vetor_d.append(vetor_b[i])
    vetor_d.append(vetor_c[i])

print(vetor_d)