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

def isPar(n):
    r = False
    if not n % 2 : r = True
    return r

def isParShort(n): 
    return True if not n % 2 else False

def isParShortPlus(n): 
    return not n % 2 

print(isPar(9))

print(isParShort(8))

print(isParShortPlus(8))