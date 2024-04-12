#Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

vetor_a = [10, 20, 5, 2, 1, 12, 15, 6, 8, 22]

soma = sum(x ** 2 for x in vetor_a)
#utilizamos uma expressão geradora (generator expression) dentro da função sum() para calcular a soma dos quadrados dos elementos do vetor. Isso percorre cada elemento do vetor, eleva-o ao quadrado e, em seguida, soma todos os resultados. Dessa forma, obtemos a soma dos quadrados dos elementos do vetor.

print(soma)