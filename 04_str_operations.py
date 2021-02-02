cadena = 'Un anillo para gobernarlos a todos'
l_c = len(cadena)
lista = cadena.split(' ')
print(lista)
print(len(lista))
print(l_c)
print(lista[0])
print(cadena[0])
lista[0] = 'EL'
print(lista)
# cadena[0] = 'E' -> error
print(cadena[-1])
print(cadena[3:9])
print(cadena[10:])
print(cadena.count('a'))