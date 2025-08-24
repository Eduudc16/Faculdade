
lista = ('zero','um','dois','três', 'quatro', 'cinco', 'seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezessei','dezessete','dezoito','dezenove','vinte')

while True:

    nro = int(input('Digite um número entre 0 e 20: '))

    if 0 <= nro <=20:
        break
    print('Tente novamente')

print(f'Você digitou o número {lista[nro]}')    
