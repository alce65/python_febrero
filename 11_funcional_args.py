def suma(*args):
    print(args)
    total = 0
    for item in args:
        total += item
    return total

def media(*data):
    media = suma(*data) / len(data)
    return media
        

t = suma(12, 45, 23, 76, 23)
m = media(12, 45, 23, 76, 23)
print(t)
print(m)

import statistics as st
print(st.mean( (12, 45, 23, 76, 23)))

def algo (**kvargs): 
    print(kvargs, type(kvargs))


algo(name='Ernesto', edad= 23)

