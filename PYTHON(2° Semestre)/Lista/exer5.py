

lista = []




while True:
    
    nota = float(input("Digite a sua idade (0 para parar): "))
    
    if nota < 0:
        
        break
    
    lista.append(nota)
    

menor = lista[0] 

total = sum(lista)

soma = len(lista)

media = sum(lista) / len(lista)


for i in lista:
    
    if i < menor:
        
        menor = i
    

print(total)
print(f'{media:.1f}')    
print(menor)

    
    
    
    
    
    
  
    

