g = 1

def use_global():
    global g
    g = g + 5 
    print('Dentro g vale', g)

use_global()
print('Fuera g vale', g)

w = 6
def ver_global(k1):
    print('Dentro k vale', k1)

ver_global(w)
print('Fuera k vale', w)


f = 0
z = 12
def inicia_global(int_f):
    int_f = int_f + 15 
    return int_f

f = inicia_global(f)
z = inicia_global(z)
print('f', f)
print('z', z)