velocidade = float(input('Digite a velocidade do vículo: '))

valor = 7.00


if velocidade > 80:
    
    multa = (velocidade - 80) * 7
    print('Você acabou recebendo multa por excesso de velocidade')
    print(f'valor da multa foi de {multa}')
    
else:
    
    print('tudo ok')