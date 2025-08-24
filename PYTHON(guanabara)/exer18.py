import math

valor = float(input('Digite o valor do ângulo: '))

seno = math.sin(math.radians(valor))
cosseno = math.cos(math.radians(valor))
tangete = math.tan(math.radians(valor))

print(f'O ângulo de {valor} tem o SENO de {seno:.2f}')
print(f'O ângulo de {valor} tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {valor} tem o TANGENTE de { tangete: 2f}')