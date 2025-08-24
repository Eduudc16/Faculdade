nro = (int(input('Digite um numero')),
       int(input('Digite um numero')),
       int(input('Digite um numero')),
       int(input('Digite um numero')))

print(f'Vocé digitou os valores{nro}')
print(f'o valor 9 apareceu {nro.count(9)}')


if 3 in nro:
    print(f'o valor 3 pareceu na posição {nro.index(3)+1}')
else:
    print('O valor 3 não foi digitado em nenhuma posição')

print('os valores pares digitados foram', end='')

for n in nro:

    if n % 2 == 0:
        print(n, end='')