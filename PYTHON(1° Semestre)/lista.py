#Questão 1: Elaborar um programa em Python que efetue o cálculo do fatorial de um número inteiro
#informado pelo usuário.


#fatorial = 1

#nro = int(input('Digite um valor: '))
#for i in range(1,nro +1):
    #fatorial *=i
    
#print(f'fatorial de {nro} é {fatorial}')  

#Questão 2: Considere o seguinte segmento de código:
#count = 5
#while count > 1:
 #print(count, end = " ")
 #count = count - 1

#for i in range(5,1,-1):
    #print(i)
    
#Questão 4: Uma rainha requisitou os serviços de um monge e disse-lhe que pagaria qualquer preço.
#O monge, necessitando de alimentos, indagou à rainha sobre o pagamento, se poderia ser feito com
#grãos de trigo dispostos em um tabuleiro de xadrez (que possui 64 casas), de tal forma que o primeiro
#quadro deveria conter apenas um grão e os quadros subsequentes, o dobro do quadro anterior. Crie
#um algoritmo para calcular o total de grãos que o monge recebeu

#graos = 1
#total = 0

#for i in range(64):
    
    #total +=graos
    
    #graos *=2
    
#print(total)    


#Questão 5: O programa DivisorProprio recebe da entrada de dados um número inteiro fornecido pelo
#usuário e mostra, na tela, um dos divisores próprios desse número. Os divisores próprios de um
#número são aqueles diferentes de 1 e do próprio número. Por exemplo, os divisores próprios de 6 são
#2 e 3. O número 5 não tem divisor próprio. O programa descrito abaixo foi desenvolvido para retornar
#o divisor próprio de um número utilizando a estrutura de repetição while

#num = int(input('Digite um número inteiro maior que zero '))
#divisor = 0

#for i in range(2,num):
    #if (num%i) == 0:
     #divisor = i
     
     
#if divisor !=0:
    #print( divisor,' é um divisor próprio de ', num)
#else:
    #print( num ,'não tem divisor próprio')



#Questão 6: Dado o conjunto de instruções a seguir:
#• Informar um valor para A e para B e exibir o resto da divisão de A por B
#Faça um algoritmo em Python com três variações, colocando o comando de repetição for
#adequadamente, de forma a:
#a) Executar o conjunto de instruções 10 vezes;
#b) Não executar nenhuma vez;
#c) Executar N vezes, onde N é uma variável informada pelo usuário.

#opcao = input('Escolha uma opção A,B,C').strip().upper()


#if opcao == "A":
    
   #for i in range(10):
        
       # a = int(input('Digite um valor: '))
        #b = int(input('Digite um valor: '))
        
        #resto = a % b
        #print(resto) 
        
#elif opcao =="B":
    
    #for i in range(0):
        
        #a = int(input('Digite um valor: '))
        #b = int(input('Digite um valor: '))
        
        #resto = a % b
        #print(resto)
        
#elif opcao =="C":
    
          #n = int(input('quantas vezes vc quer repetir: '))
          
          #for i in range(n):
              
              #a = int(*input('Digite um valor: '))
              #b = int(*input('Digite um valor: '))
              
              
              #resto = a % b
              #print(resto)
              
              
vetor = [1,2,3,4,5]

vetor.append(6)
vetor.insert(6,7)
vetor.remove(2)
vetor.sort(reverse=True)



print(vetor)                        