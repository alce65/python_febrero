class Persona():
    num_pers = 0
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self._edad = edad
        self.__estudios = None
    
    def saludar(self):
        self.saludos = 1
        print(f'Hola soy {self.nombre}, y tengo {self._edad} años')

    def saludar_a(self, alguien = 'amigo'):
        print(f'Hola {alguien}, soy {self.nombre}, y tengo {self._edad} años')

    def edad(self, edad = None):
        if edad: self._edad = edad
        return self._edad    

############################################################
p1 = Persona('Pepe', 23) 
Persona.num_pers +=  1
p2 = Persona('Elena', 32)

print(type(p1), p1.nombre)
print(type(p2), p2.nombre)
p1.saludar()
p2.saludar_a(p1.nombre)

print(p1._edad) # No se debe
# print(p1.__estudios) # AttributeError: No se puede acceder ....
print(p1._Persona__estudios) # ... o si, de forma exspecial

p1.nombre = 'Jose'
print(p1.nombre)

p1._edad = 24 # No de debe
print(p1.nombre, p1._edad)

p1._Persona__estudios = 'Informatica'
print(p1._Persona__estudios) 

p1.altura = 180
print(p1.altura)

print(isinstance(p2, Persona))
print(isinstance(p1, Persona))

print(p2.edad())
print(p2.edad(33))

