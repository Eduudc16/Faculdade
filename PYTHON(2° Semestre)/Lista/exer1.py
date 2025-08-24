

lista = []
contador = 0

while contador < 5:
       
     nro = int(input(f'Digite o {contador + 1}° número '))
      
     lista.append(nro)
     contador += 1
     
     
buscar = int(input('Qual núemro deseja procurar? '))
     
     
if buscar in lista:
    print(f"O número {buscar} está na lista.")
else:
    print(f"O número {buscar} não está na lista.")

     
     
    