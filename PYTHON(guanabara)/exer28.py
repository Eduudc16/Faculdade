import random

nro = random.randint(0,5)

tentativa = int(input('Tente adivinhar um número entre 0 e 5: '))

if tentativa == nro:
    
    print(f'Você acertou o número !!!!!!!!!!')
    
else:
    
    print('Você acabou errado ')



