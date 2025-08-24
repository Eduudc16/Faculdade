preco = float(input('Digite o valor pago: '))

print('''FORMAS DE PAGAMENTO
      
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais co cartão''')

opção = int(input('Qual é a o opção'))  


if opção == 1:
    
    total = preco - (preco * 10 /100)  
    print(f'Sua compra de R${preco: .2f} vai custar R${total: .2f}')
    
elif opção == 2:
    total = preco - (preco * 5 /100) 
    print(f'Sua compra de R${preco: .2f} vai custar R${total: .2f}')
    
elif opção == 3:
    total = preco
    parcela = total / 2
    print(f'Sua compra sera parcelada em 2x de R$ {parcela:.2f}')
      
elif opção == 4:
    total = preco + (preco * 20 / 100)
    totalpar = int(input('Quantas parcelas ? '))
    parcela = total / totalpar
    print(f'sua compra de R$ {preco: .2f} vai custar R$ {total: .2f} no final.s')
else:
    
    total = preco
    print('OPÇÃO INVÁLIDA de pagamento')
    
print(f'Sua compra de R${preco: .2f} vau custar R${total: .2f} no final')    
      
      
      
      

      
 


