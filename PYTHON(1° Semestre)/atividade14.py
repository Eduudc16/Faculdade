vetorc = []

for i in range(10):
    valor = input("informe uma letra ")
    if valor not in ('a','e','i','o','u'):
        
        vetorc.append(valor)

print(vetorc)


tamanho = len(vetorc)
print(f'total de consoantes {tamanho}')        