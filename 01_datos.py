# Tipos básicos

x = 'Hola'
print(x, type(x))

# Tipado dinámico
x = 34
print(x, type(x))

# Tipado estático: OTROS LENGUAJES
# x: int
# x = 'Pepe' -> error

x = 34.78
print(x, type(x))

x = True
print(x, type(x))

x = False
print(x, type(x))

x = None
print(x, type(x))

# Tipos complejos

c = ['Pepe', 23, True]
print(c, type(c)) # Listas, array

c = ('Pepe', 23, True)
print(c, type(c)) # Tupla, array inmutable

c = {'Pepe', 23, True, 23}
print(c, type(c)) # Set, array de elementos únicos

c = {'nombre': 'Pepe', 'edad': 23, 'isAlumno': True}
print(c, type(c)) # dic, arry asociativos, hash, objetos literales POJO
