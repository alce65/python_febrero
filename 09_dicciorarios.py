animales = ['Perro', 'Ornitorrinco', 'Gato', 'Canario' ]

animales_dic = {'Perro':'guau', 'Ornitorrinco':'Hola', 'Gato':'miau', 'Canario':'pio' }
animales_dic2 = dict(Perro = 'guau', Ornitorrinco ='Hola', Gato ='miau', Canario ='pio')

print(animales_dic)
print(animales_dic2)

print(animales_dic.items())
print(animales_dic.keys())
print(animales_dic.values())

for k, v in animales_dic.items() :
    print (f'El {k} dice {v}')
print('Final') 

print(animales_dic['Perro'])
# print(animales_dic['Caballo']) -> KeyError

print(animales_dic.get('Perro'))
print(animales_dic.get('Caballo'))

animales_dic['Caballo']="hiii"
animales_dic.update({'Oveja':'Bee'})
print(animales_dic)

item = animales_dic.pop('Perro')
print(animales_dic)
print(item)