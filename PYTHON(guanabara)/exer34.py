salario = float(input('Digite o seu sálario'))


if salario <= 1250:
    
    aumento = salario +(salario * 15 / 100)
    
    print(aumento)
    
else:
    
     aumento = salario +(salario * 10 / 100)
    
     print(aumento)