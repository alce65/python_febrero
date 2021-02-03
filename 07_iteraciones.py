i = 0
while i <= 5:
    print(i)
    i += 1
print('Final')

print('------------')

for i in range(0,6):
    print(i)
print('Final')

for item in 'range':
    print(item)
print('Final')
    

paises = ['España', 'Colombia', 'Francia']
i = 0
for item in paises:
    i += 1
    print(i, item)
print('Final')    
    
user = {'nombre': 'Pepe', 'edad': 23, 'isAlumno': True}
for k, v in user.items():
    print (k, v)
print('Final')  

users = [{'nombre': 'Pepe', 'edad': 23, 'isAlumno': True},
        {'nombre': 'Elena', 'edad': 24, 'isAlumno': True}]

print('=======')
for user in users:
    for k, v in user.items():
        print (k, v)
    print('----')
print('Final')  