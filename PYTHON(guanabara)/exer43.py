peso = float(input('Digite o seu peso ? (KG) '))

altura = float(input('Qual é sua altura ? (m) '))


imc = peso / (altura * altura)


if imc < 18.5:
    
    print(f'Seu imc é {imc:.2f} você está abaixo do peso')
    
elif imc >= 18.5 and imc <25:
    
    print(f'Seu imc é de {imc:.2f} você esta no peso ideal')
    
    
elif imc >= 25 and imc < 30:
    
     print(f'Seu imc é de {imc:.2f} você está sobrepeso')
     
elif imc >= 30 and imc < 40:
    
     print(f'Seu imc é de {imc:.2f} você está Obesidade')
     
else:
    
     print(f'Seu imc é de {imc:.2f} você está Obesidade mórbida')
     
     
     
     