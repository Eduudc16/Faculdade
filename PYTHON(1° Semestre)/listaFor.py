#Questão 1: Elaborar um programa em Python que efetue o cálculo do fatorial de um número inteiro
#informado pelo usuário.


#fatorial = 1

#nro = int(input('Digite um valor '))

#for i in range(1,nro + 1):
    
    #fatorial *= i

#print(f'O fatorialde de {nro} é {fatorial}')   


#2: Considere o seguinte segmento de código:

#Reescreva o código acima e substitua o loop while pelo loop for 

#for i in range(5,1,-1):
    #print(i)
    
    
    
#Questão 4: Uma rainha requisitou os serviços de um monge e disse-lhe que pagaria qualquer preço.
#O monge, necessitando de alimentos, indagou à rainha sobre o pagamento, se poderia ser feito com
#grãos de trigo dispostos em um tabuleiro de xadrez (que possui 64 casas), de tal forma que o primeiro
#quadro deveria conter apenas um grão e os quadros subsequentes, o dobro do quadro anterior. Crie
#um algoritmo para calcular o total de grãos que o monge recebeu.    

#total = 0
#graos = 1

#for i in range(64):
    #total += graos
    #graos *=2
    
#print('Total de grãos que o monge receberia: ', total)     



#total = 0
#graos = 1

#for i in range(64):
    
    #total += graos
    
    #graos *= 2
    
#print(total)   


print("Escolha uma das opções:")
print("a) Executar 10 vezes")
print("b) Não executar nenhuma vez")
print("c) Executar N vezes (informado pelo usuário)")

opcao = input("Digite a opção (a, b ou c): ").lower()


if opcao == 'a':
    
    for i in range(10):
       print(f"\n[{i+1}/10]")
       a = int(input("Digite o valor de A: "))
       b = int(input("Digite o valor de B: "))
       
       
       if b !=0:
            print("Resto da divisão A % B =", a % b)
       else:
            print("Divisão por zero não é permitida.")
        
elif opcao == 'b':
     for i in range(0):
       
       a = int(input("Digite o valor de A: "))
       b = int(input("Digite o valor de B: "))
       
       
       if b !=0:
            print("Resto da divisão A % B =", a % b)
       else:
            print("Divisão por zero não é permitida.")
            
            
elif opcao =='c':
    
    n = int(input('Quantas vezes você quer repedir? '))
    
    for i in range(n):
       print(f"\n[{i+1}/10]")
       a = int(input("Digite o valor de A: "))
       b = int(input("Digite o valor de B: "))
       
       
       if b !=0:
            print("Resto da divisão A % B =", a % b)
       else:
            print("Divisão por zero não é permitida.")

else:
    print('opção inválida')
               



 




