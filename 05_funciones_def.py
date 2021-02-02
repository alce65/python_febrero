def suma(a,b): # parámetros
    r = a + b
    return r

# Mala práctica por mezclar distintas funcionalidades
def suma_y_muestra(a,b):
    def sum (a,b):
        return a+b
    r = sum(a,b)
    print(r)

print(type(suma))

indice = 6 
print(suma(3,indice)) #pasamos argumentos
suma_y_muestra(8,75)

def resta(a = 0, b = 0): # parámetros
    r = a - b
    return r

print(resta())
print(resta(5))
print(resta(0,5))
# print(resta(0,5,9)) -> error
