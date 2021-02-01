x = '12'
y = 3
z = 4
print(x, type(x))
print(y, type(y))
print(z, type(z))

print('y + z', y + z)
# print('x + y', x + y) -> error

# Tipado debil (JS) -> casting implicito (o coerción) x + y = '123'

# Tipado fuerte -> NO HAY casting implicito
# TypeError: can only concatenate str (not "int") to str

print('x + y', x + str(y))
print('x + y', int(x) + y)

print(x, type(x))
print(y, type(y))
print(z, type(z))

a = 12
b = 2.4
c = 0
print(a, type(a))
print(b, type(b))

print('a*b', a*b)
print('a*b', a*int(b))

print(not a)
print(not c)

print(not not a)
print(not not c)

print(bool(a))
print(bool(c))