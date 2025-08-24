## 1 F.U.P para somar dois números e exibir o resultado da soma. O usuário deverá informar os dois números.


nr1 = int(input('fale um número: '))
nr2 = int(input('fale um número: '))

soma = nr1 + nr2

print(soma)



# 2 F.U.P para ler uma temperatura em Celsius e converter para fahrenheit.

celsius = float(input('Informe a temperatura em Celsius: '))
fahrenheit = (celsius * 9/5) + 32
print(f'A temperatura em Fahrenheit é: {fahrenheit:.2f}')

# 3 F.U.P para conversão de metros para centimetors. Informe um valor em metros e converta para centímetros.

metros = float(input('Informe um valor em metros: '))
centimetros = metros * 100
print(f'O valor em centímetros é: {centimetros:.2f}')

# 4) F.U.P para informar 4 notas de um aluno e calcule a média aritmética

soma = 0

for i in range (4):
 nota = float(input('Digite a sua nota:'))
 soma += nota

media = soma / 4
print(media)

# 5) F.U.P para informar um número e mostrar se ele é positivo ou negativo.


nro = float(input('Digite um valor'))

if nro > 0:
    
    print('Número positivo')

elif nro < 0:
    
    print('Número negativo')    
    
else:
    
    print('tentativa negada')    

# 6) F.U.P que um número e diga se ele é positivo, negativo ou zero.

nro = float(input('Digite um valor'))

if nro > 0:
    
    print('Número positivo')

elif nro < 0:
    
    print('Número negativo')
    

elif nro == 0:
    
    print('O número e zero')        
    
else:
    
    print('tentativa negada') 
    
#7) F.U.P que peça um número inteiro e exiba se ele é par ou ímpar. 
 
nro = int(input('Digite um valor: '))

if nro % 2 == 0:
    
    print('É e par')
    
else:
    
   print('é ímpar')
   
# 8) F.U.P que Leia três números e exiba o maior.

maior = None

for i in range(3):
    nro = int(input('Digite um valor: '))
    if (maior is None) or (nro > maior):
        maior = nro

print(f'O maior número digitado foi: {maior}')

#9) F.U.P que informe a idade de uma pessoa e classifique-a como
#criança (0-12), adolescente (13-17) ou adulto (18+). 


idade = int(input('Digite a sua idade: '))

if idade >= 0 and idade <=12:
    
    print('Criança')
    
elif idade >= 13 and idade <=17:
    
    print('Adolescente')   
    
else:
    
    print('adulto')    


#10) F.U.P que peça o valor de uma compra e aplique um desconto
#de 10% se for acima de R$ 100,00.


compra = int(input(' digite o valor de compra: '))

if compra >= 100:
    
    desconto = compra * 0.10
    
    valor = compra - desconto
    
    print(valor)
    
else:
    
    print(f'o valor da sua compra foi s{compra}')    
  
#11) F.U.P que peça um número e exiba a tabuada de 1 a 10 desse
#número.

nro = int(input('Digite um valor: '))

for i in range(1,11):
    
    multi = nro * 1
    multi *= i
    
    print(f'{i} X {nro} = {multi} ')    
          
#12)F.U.P que faça a soma dos primeiros 10 números naturais:
#Calcule a soma de 1 a 10 usando um loop.          
    
soma = 0 

for  i in range (1,11):
    soma += i

print(soma)

#13) F.U.P que peça um número e faça uma contagem regressiva
#até zero.

nro = int(input('Digite um valor: '))

for i in range(nro, -1, -1):
    print(i)
    
#14) F.U.P que gere um número aleatório de 1 a 100 e peça ao
#usuário para adivinhar, dando dicas de "maior" ou "menor" até
#acertar 

import random

numero_secreto = random.randint(1, 100)
palpite = 0

while palpite != numero_secreto:
    palpite = int(input('Adivinhe o número entre 1 e 100: '))
    if palpite < numero_secreto:
        print('Maior')
    elif palpite > numero_secreto:
        print('Menor')

print('Parabéns! Você acertou o número.')