animales = ['Perro', 'Ornitorrinco', 'Gato', 'Canario' ]
print(animales)
print(animales[0])
print(animales[1:3])
print(animales[:2])

i = animales.index('Ornitorrinco')
print(i)

animales[i] = 'Koala'
print(animales)

animales.append('Tortuga')
animales.insert(2,'Liebre')
print(animales)

animales.remove('Gato')
# animales.remove('Raton')
item = animales.pop(1)
print(animales)
print(item)


cadena = 'Un anillo para gobernarlos a todos'

lista = cadena.split(' ')
print(lista)
lista.reverse()
cadena2  = ' - '.join(lista)
print(cadena2)

# tanimales = ('Perro', 'Ornitorrinco', 'Gato', 'Canario' )
tanimales = tuple(animales)
print(tanimales)
print(tanimales.count('Gato'))
print('Gato' in tanimales)


