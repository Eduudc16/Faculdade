from datetime import date

atual = date.today().year

nascimento = int(input('em que ano vc nanceu:'))

idade = atual - nascimento

if idade <= 9:
    
    print('MIRIM')
    
elif idade >=9 and idade <= 14:
    
    print('INFANTIL')
    
    
elif idade >= 14 and idade <= 19:
    
    print('JUNIOR')
    
elif idade >19 and idade <25:
    
    
    print('SÊNIOR')
    
else:
    
    print('MASTER')
    
    