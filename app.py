numero = input('Pasa el número: ')

cont = 0
for i in range(numero):
    if numero % i == 0:
        cont = cont  +1

if cont == 2:
    print('el número ', numero, ' es Primo.')
else:
    print('el número ', numero, ' No es primo.')