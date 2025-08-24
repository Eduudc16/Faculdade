casa = float(input('Digte o valor da casa: '))
salario = float(input('Digite o seu sálario: '))
anos = int(input('Quantos anos de financiamento: '))

prestacao = casa / (anos * 12)
minimo = salario * 30 / 100


if prestacao <= minimo:
    
    print('Emprestimo aceito')
    
else:
    print('negado')
