edad = 56
#....
resistencia = 56

print(edad, id(edad))
print(resistencia, id(resistencia))

resistencia = 55

print(edad, id(edad))
print(resistencia, id(resistencia))

origen = 'España'
paises = ['España', 'Colombia', 'Francia']

print(origen, id(origen))
print(paises[0], id(paises[0]))

paises[0] = 'Portugal'

print(origen, id(origen))
print(paises[0], id(paises[0]))