

lista = []


for i in range(3):
    
    nro = int(input('Digite um número: '))
    
    lista.append(nro)
    
    
maior = lista[0]
menor = lista[0]

for nro in lista:
    
    if nro > maior:
        maior = nro
    if nro < menor:
        menor = nro
    
    
print("Maior:", maior)
print("Menor:", menor)    
    
    