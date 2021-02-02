print(3 + 4)
print(3 - 4)
print(3 * 4)
print(4 // 3)
print(4 % 3)
print(4 / 3)
print(3 ** 4)
print((3 + 4) * 2)

x = 8
x += 2 # x = x + 2

d = 0
e = 2

print(d == e)
print(d != e)
print(d > e)
print(d >= e)
print(d < e)
print(d <= e)

print('Pepe' < 'Valerio')

a = [1,2,3]
a1 = a
b = [1,2,3]

print(a == a1)
print(a == b)

print(id(a))
print(id(a1))
print(id(b))

print(a is a1)
print(a is b)

d = 0
e = 2
a = 10

print(a != d and d > e)
print(d > e and a != d)
print(a != d or d > e)
print(d > e or a != d)

print(12 and 23)
print(12 or 23)

def suma(a,b): # parámetros
    r = a + b
    return r

print(a == d and suma (2,34))
print(a != d and suma (2,34))

print(a != d and  d > e)
print(a != d and not  d > e)

print(not 'Pepe')
