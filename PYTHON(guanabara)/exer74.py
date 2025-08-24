from random import randint

numero = (randint(0,5),randint(0,5),randint(0,5),randint(0,5),randint(0,5))

print('Os valores sorteados foram:', end=' ')
for i in numero:
    print(i, end=' ')


print(f'\nO valor número dentro da tuplha é {max(numero)}')    
print(f'O valor número dentro da tuplha é {min(numero)}')    
