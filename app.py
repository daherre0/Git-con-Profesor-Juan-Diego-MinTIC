numero = int(input('Pasa el número: '))

cont = 0
for i in range(2, numero + 1):
    if numero % i == 0:
        cont = cont  +1

if cont == 1:
    print('el número ', numero, ' es Primo.')
else:
    print('el número ', numero, ' No es primo.')