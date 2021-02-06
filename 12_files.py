
def read_file(fname):
    try:
        f = open(fname, 'rt')
        text = f.read()
    except FileNotFoundError:
        text = f'No existe el fichero {fname}'
    return text
import os

print(read_file('sample.txt'))
print(read_file('sample2.txt'))

try:
    file_name = 'new_sample2.txt'
    f = open(file_name, 'xt')
    f.write('Esto es un fichero creado desde Python')
    print('Creado el fichero', file_name)
    f.close()
except FileExistsError:
    print('El fiche ya existe')

print(read_file(file_name ))

os.remove(file_name)

