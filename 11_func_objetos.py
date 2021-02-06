def suma(a = 0, b = 0): # parámetros
    r = a + b
    return r

def resta(a = 0, b = 0): # parámetros
    r = a - b
    return r

print(type(suma))
print('<class \'function\'>')

print(2+2)
print(4)

y = suma
print(y(3,5))


def calcular(a, b, callback ):
    print(callback(a,b))

calcular(3, 8, suma)
calcular(3, 8, resta)
calcular(3, 8, lambda a,b: a*b)

div = lambda a,b: a/b

print(div(3,5))

def multiplicador(n):
    return lambda a : a * n 

duplicar = multiplicador(2)
triplicar =  multiplicador(3)

print(duplicar(12))
print(triplicar(12))