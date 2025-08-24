

lista = [1,5,7,3,8]

maior = lista[0]

menor = lista[0]

for nro in lista:
    
    if nro > maior:
       maior = nro
       
    if nro < menor:
       menor = nro
       
       
       
print(f'O maior é {maior} e o menor é {menor}')
