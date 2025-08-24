nro = int(input('Digite um valor: '))

unidade = nro // 1 % 10
dezena = nro // 10 % 10
centena = nro // 100 % 10
milhar = nro // 1000 % 10

print(f'Unidade: {unidade}')
print(f'Dezena: {dezena}')
print(f'Centena: {centena}')
print(f'Milhar;S {milhar}')

