def dividir(a,b):
    try:
        r = a / b
        return r
    except ZeroDivisionError:
        print('No se puede dividir por 0')    
    except Exception as err:
        print('Error', type(err).__name__ )
    
print(dividir(7,2))
r = dividir(7,0)
if r != None: print(r)

try:
    print(dividir(7))
except TypeError as err:
    print('Error', type(err).__name__ )
