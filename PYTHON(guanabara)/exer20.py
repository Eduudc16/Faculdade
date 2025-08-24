import random

lista = []
for i in range(4):
    
    nome = input('Digite o nome do aluno: ')
    
    lista.append(nome)
    
random.shuffle(lista)    
print(lista)
