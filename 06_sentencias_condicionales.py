x = 0
x = 2

y = ''
if x == 0:
    print('x no vale nada')
elif x > 0:
    print('x es positivo')
    if y == 'M':
        print('Hola chico')
    else:
        print('Hola chica')
else:
    print('x es negativo')

if x == 0:
    print('x no vale nada')
elif x > 0 and y == 'M':
    print('x es positivo')
    print('Hola chico')
elif x > 0 and y != 'M':
    print('x es positivo')
    print('Hola chica')
else:
    print('x es negativo')