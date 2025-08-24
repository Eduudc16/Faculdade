nro = int(input('Digite o número'))
nr2 = int(input('Digite o número'))

maior = 0
menor = 0

if nro > nr2:
    
    maior = nro
    menor = nr2
    
elif nro < nr2:
    
    maior = nr2
    menor = nro
    
elif nro == nr2:
    
    print('Eles são iguais')

else:
    
    print('Inválido')
    
    
    
    
print(maior)
print(menor)    