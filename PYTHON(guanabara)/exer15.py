Km_percorrido = float(input('Quantos km percorridos: '))
dias_quandida = int(input('Qunatos dias foi alugado: '))


pago = (Km_percorrido * 0.15) + (dias_quandida * 0.15)
print(f'O total a pagar é de R$:{pago:.2f}')