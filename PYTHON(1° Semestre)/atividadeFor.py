#Exercício 1:
#Faça um programa que mostre na tela os números de 100 a 0

#----------------------------
#for i in range(100,0,-1):
    #print(i-1)
#----------------------------
    
#Exercício 2: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50


#---------------------------
#for i in range (1,51):
    
    #if i % 2 ==0:
       # print(i)
#----------------------------

#Exercício 3: Faça um programa que calcule a soma entre todos os números impares  que são múltiplos de três (3) e que se encontram no intervalo de 1 até 500.

#----------------------------
#soma = 0
#for i in range(1,500):
    
    #if i % 3 == 0:
        
        #soma += i

#print(soma)
#----------------------------

#Exercício 4: Faça um programa para exibir a tabuada de um número informado pelo usuário (utilize estrutura de repetição for)

#nro = int(input("Digite um número "))

#-------------------------------
#for i in range(1,11):
    
    #soma = nro * i
    #print(f'{nro} * {i} = {soma}')
#---------------------------------    
        
#Exercício 5: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares Se o valor digitado for ímpar, desconsidere-o.

#-----------------------------
#soma = 0
#for i in range(1,7):
    #nro = int(input("Digite um número "))
    
    #if nro % 2 == 0:
        #soma += nro
        
#print(soma)

#---------------------------------
          
#Exercício 6: Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão.

#------------------------------------------------------------    
#comeco = int(input("Digite o valor que vai começar "))    
#razao = int(input("razão dele "))

#print("Os 10 primeiros termos da PA são:")

#for i in range(10):
    #termo = comeco + i * razao
    #print(termo)
#-------------------------------------------------------------   

#Exercício 7: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo

#-------------------------------------------------
#nro = int(input('Digite um valor'))
#divisor = 0

#for i in range(1,nro,+1):
    #if nro % i == 0:
        #divisor += 1    
        
#if divisor == 2:
    #print(f"{nro} é um número primo.")
#else:
    #print(f"{nro} não é um número primo.") 
    
#---------------------------------------------------           


#Exercício 8: Crie um programa que leia o ano de nascimento de sete pessoas No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. Pesquise uma função no python que retorna o ano corrente

#----------------------------------------------------------------------
#from datetime import datetime

#ano_atual = datetime.now().year
#maior = 0
#menor = 0
#for i in range(3):
    
    #ano_nascimento = int(input('em que ano você nasceu '))
     
    #idade = ano_atual - ano_nascimento
   
    #if idade >= 18:
        #maior += 1 
    #else:
        #menor += 1    
        
#print(f'pessoa que são maiores de idade são {maior}')   
#print(f'pessoa que são menores de idade são {menor}')

#----------------------------------------------------------------       

#Exercício 9: Faça um programa que leia o peso de cinco pessoas No final, mostre qual foi o maior e o menor peso lidos

#-----------------------------------------------------------------------
#maior = 0
#menor = 0 
#for i in range(1,4):
    
    #peso = float(input(f"Digite o peso da {i}ª pessoa (em kg): "))
    
    #if i == 1:
        
        #maior =  peso
        #menor =  peso
    #else:
        #if peso > maior:
            #maior = peso
        #if peso < menor:
            #menor = peso
                
#print(maior)
#print(menor)    
#----------------------------------------------------------------------------

#Exercício 10: Desenvolva um programa que leia nome, idade e sexo de 4 pessoas
# No final do programa, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres têm menos de 20 anos

#soma = 0
#Homemidade = 0
#HomemNome = 0
#MulhorIdade = 0
#for i in range(1,5):
    
    #print(f"\n----- {i}ª PESSOA -----")
    #nome = input('Digite o seu nome ')
    #idade = int(input('Digite a sua idade '))
    #sexo = input('Seu sexo ').upper()
    
    #soma += idade
    
    #if sexo == 'M':
        #if idade > Homemidade:
           # Homemidade = idade
            #HomemNome = nome
            
    #elif sexo == 'F':
        #if idade < 20: 
         #MulherIdade += 1
         
#media = soma / 4 

#print(f"\n→ A média de idade do grupo é: {media:.1f} anos")
#if HomemNome:
    #print(f"→ O homem mais velho é {HomemNome} com {Homemidade} anos")
#else:
    #print("→ Não há homens no grupo.")
#print(f"→ Total de mulheres com menos de 20 anos: {MulherIdade}")     




#nro = int(input('Digite um número'))
#divisor = 0

#for i in range(2,nro):
    
    #if nro % i == 0:
        #print(i)
        #divisor = True
 
#if not divisor:
     #print('Nenhum. Número é primo ou igual a 1.')
 
 
 
#fatorial = 1
#nro = int(input('Digite um número: '))
#for i in range(1,nro + 1):
    
    
    #fatorial *= i
    
#print(fatorial)

pares = []
impares = []
primos = []

qltpares = 0
qltimpares = 0
qltprimos = 0

for i in range(5):
    
    nro = int(input('Digite um número: '))
    
    if nro % 2 == 0:
         
         qltpares +=1
         
         pares.append(nro)
    
    elif nro % 3 == 0:
        
        qltimpares +=1
        
        impares.append(nro)
        
    elif nro > 1:
        divisores = 0
        for j in range(1, nro + 1):
            if nro % j == 0:
                divisores += 1
        if divisores == 2:
            qltprimos += 1
            primos.append(nro)   
        
print("Quantidade de pares:", qltpares)
print("Quantidade de ímpares:", qltimpares)
print("Quantidade de primos:", qltprimos)

print("Pares:", pares)
print("Ímpares:", impares)
print("Primos:", primos)       