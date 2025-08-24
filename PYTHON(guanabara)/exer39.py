from datetime import date

atual = date.today().year

nascimento = int(input('em que ano vc nanceu:'))



idade = atual - nascimento

if idade == 18:
    
    print('Você tem que se alistar Imediatamente!!')
    
elif idade < 18:
    saldo = 18 - idade
    
    ano = atual + saldo
    
    print(f' Ainda faltam {saldo} para o alistamento')
    
    print(f'Você precisa se alistar daqui a {ano}')
    
elif idade > 18:
    
     saldo =  idade - 18 
     
     ano = atual - saldo
     
     print(f' Você deveria ter se alistado há {saldo}')
     
     print(f'Seu alistamento foi em  {ano}')