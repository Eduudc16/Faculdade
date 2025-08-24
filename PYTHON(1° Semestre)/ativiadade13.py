#Faça uma programa que leia um vetor de 5 números:
#inteiros e mostre-os

par = []
impar = []

for i in range (5):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print(par)
print(impar)