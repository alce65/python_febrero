x = 'Cadena de "caracteres" en \'Phyton\''
y = "Cadena de 'caracteres' \nen dos líneas"

z = 'Cadena de caracteres\n' + \
'en dos líneas'

m = '''Cadena de "caracteres"
en 'dos' líneas 😊'''

print(x)
print(y)
print(z)
print(m)

a = 'hola'
b = 'Hola mundo'
print(a.upper())
print(a.capitalize())
print(b.lower())
print(b.title())

cad = ' Cadena de "caracteres" en Phyton '
lista = cad.split(' ')
print(lista)

print(a.upper().startswith('H'))
print(cad.strip())