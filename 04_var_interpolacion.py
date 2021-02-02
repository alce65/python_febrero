lenguaje = 'Python'
autor = 'Guido'

msg = 'El lenguaje ' + lenguaje + ' fue creado por ' + autor
print(msg)

i_msg = 'El lenguaje {} fue creado por {}'.format(lenguaje,autor)
print(i_msg)

i_msg = 'El lenguaje {leng} fue creado por {autor}'.format(autor=autor,leng=lenguaje)
print(i_msg)

i_msg = 'El lenguaje %s fue creado por %s' % (lenguaje,autor)
print(i_msg)

i_msg = f'El lenguaje {lenguaje} fue creado por {autor}'
print(i_msg)
