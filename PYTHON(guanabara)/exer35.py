a = float(input('Digite o valor: '))
b = float(input('Digite o valor: '))
c = float(input('Digite o valor: '))

if a < b + c and b < a + c and c < a + 3:
    print('é um triangulo')
    
else:
    
    print('não é um trinagulo')