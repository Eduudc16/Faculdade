ano = int(input('Que ano quer analisar? '))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto')
    
else:
    print(f'O ano {ano} não é bissexto')