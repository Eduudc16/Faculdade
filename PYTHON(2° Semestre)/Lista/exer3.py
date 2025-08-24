
def classificar(idade):
    
     if idade <= 12:
         
         return('Criança')
         
     elif idade >= 13 and idade <=17:
         
         return('Adolecente')
         
     elif idade >= 18 and idade <= 59:
         
         return('Adulto')
         
     else:
         
         return('idoso')
     
lista = []
classificacao = []    
     
while True:
    
    idade = int(input("Digite a sua idade (0 para parar): "))
    
    if idade == 0:
        
        break
    
    lista.append(idade)
    classificacao.append(classificar(idade))
    
for i,j in zip(lista,classificacao):
    
    print(f'Idade: {i}: {j}')   

    