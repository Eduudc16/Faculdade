nro = int(input('Digite um número'))

escolha = int(input('Escolha uma das bases para coversão:'))

if escolha == 1:
    
    print(bin(nro)[2:])
    
elif escolha == 2:
    
    print(oct(nro)[2:])
    
    
elif escolha == 3:
    
    print(hex(nro)[2:])

else:
    
    print('errado')