#num = [2,5,9,1]
#num[2] = 3
#num.append(7)
#num.sort(reverse=True)
#num.insert(2,0)
#num.pop(2)

#print(num)
#print(f'Essa lista tem {len(num)} elementos.')


#Faça um programa que possua um vetor denominado A que armazene 6 números inteiros. O programa deve executar os seguintes passos:
#(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
#(b) Armazene em uma variável inteira (simples) a soma entre os valores das posições
#A[O], A[1] e A[5] do vetor e mostre na tela esta soma.
#(c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
#(d) Mostre na tela cada valor do vetor A, um em cada linha.

#-------------------------------------------------------------------------------
#vetor = [1,0,5,-2,-5,7]

#soma = vetor[0] + vetor [1]
#print("Soma dos valores A[0], A[1] e A[5]:", soma)

#vetor[4] = 100

#print("\nValores do vetor A:")

#for i in vetor:
   #print(i)
   
#---------------------------------------------------------------------------------

# 2 Crie um programa que lê 6 valores inteiros e, em seguida, mostre na tela os valores lidos.

#-------------------------------------------------------------
#vetor = []

#for i in range (1,7):
    
    #nro = int(input('Digite um valor '))
    #vetor.append(nro)

#print("\nValores digitados: ")

#for i in vetor:
    #print(i)
    
#--------------------------------------------------------------    


#3 Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado das
#componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos têm
#10 elementos cada. Imprimir todos os conjuntos.

#pares = []
#impares = []

#for i in range(1,6):
    
    #nro = int(input('Digite um número '))
    
    #if nro % 2 == 0:
        
       # pares.append(nro)
    #else:
        
        #impares.append(nro)

#print(pares)
#print(impares)


#def verificar_pessoa(nome,idade,sexo):
    #sexo = sexo.strip().upper()
    
    #if sexo == 'M':
        #print(f'Nome: {nome}, Sexo: homem, idade: {idade}')
    #elif sexo == 'F':
        #print(f'Nome: {nome}, Sexo: mulher, idade:{idade}')
    #else:
        #print(f'Nome: {nome}, Sexo inválido.')    
       
#names = []
#ages = []
#sexes = []

#for i in range(1, 4):
    #nome = input('Digite o seu nome: ')
    #idade = int(input('Digite a sua idade: '))
    #sexo = input('Digite o seu sexo (M/F): ').strip().upper()
    
    #names.append(nome)
    #ages.append(idade)
    #sexes.append(sexo)
    
#print("\nHomens cadastrados:")

#for i in range(len(sexes)):
    #verificar_pessoa(names[i], ages[i],sexes[i])
    
 

#nomes = [ ]

#for i in range(3):
    
    #nome = input('Digite seu nome')
    
    #nomes.append(nome)
    
    #nomes.sort()

    #print(nomes) 
    
    
#multi = 1
    
#nro = int(input('Digite um número: '))

#for i in range(1,11):
    
    #multi = nro * i
    
    #print(f'{nro} X {i} = {multi}')  
    
 

#fatorial = 1

#nro = int(input('Digite um valor '))

#for i in range(1,nro +1):
    
    #fatorial *= i
          
    
#print(fatorial)    
        
        
        
        
        







