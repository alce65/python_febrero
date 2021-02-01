x = 3
print(x, type(x), id(x))

l = ['Pepe', 'Juan', 'Elena']
print(l, type(l), id(l))

# Variable inmutable => referencia nueva
x = 23
print(x, type(x), id(x))

# Variables mutables => cambian sin cambiar de referencia
l[0] = 'Jose'
print(l, type(l), id(l))

l = ['Jose', 'Juan', 'Elena']
print(l, type(l), id(l))