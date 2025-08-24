distancia = float(input('Digite quantos km você andou: '))

curtas = 0.50
longas = 0.45

if distancia <= 200:
    
    valorPagar = distancia * curtas
    
    print(f'Valor apagar {valorPagar}')
    
else:
    
    valorPagar = distancia  * longas
    
    print(f'Valor apagar {valorPagar}')