animales = ['Perro', 'Ornitorrinco', 'Gato', 'Canario' ]

i = 0
for animal in animales:
    if animal.lower() == 'ornitorrinco':
        continue
    print(animal)

print('=========')

passw = 'ornitorrinco'
userPass = ''
i = 1
while (userPass != passw ):
    userPass = input('Escribe la contraseña: ')
    if i >= 3:
        print('Demasiados intentos')
        break
    i += 1
else:
    print('Saludo, ya estas dentro')