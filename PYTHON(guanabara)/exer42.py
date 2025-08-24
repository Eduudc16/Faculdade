r1 = float(input('Digite o valor do segmento: '))
r2 = float(input('Digite o valor do segmento: '))
r3 = float(input('Digite o valor do segmento: '))


if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('é um triangulo')
    
    if r1 == r2 == r3:
        
        print('Equilátero')
        
    elif r1 != r2 != r3 != r1:
        
        print('Escaleno')
        
    else:
        
        print('Isósceles')
        
    
else:
    
    print('não é um trinagulo')