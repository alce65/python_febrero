class Persona():

    def __init__(self, nombre, correo, edad):
        self.__nombre = nombre
        self.__correo = correo
        self.__edad = edad
    
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre
    
    def getEdad(self):
        return self.__edad

    def saludar(self, aQuien = 'amigo'):
        print('Hola {}, soy {}'.format(aQuien, self.__nombre))

    def cumplirAnnos(self):
        self.__edad += 1
        print('Ya tengo {} años'.format(self.__edad))

class Alumno(Persona):
    
    def __init__(self, nombre, correo, edad, curso):
        super(Alumno, self).__init__(nombre, correo, edad)
        self.__curso = curso

    # Polimorfismo
    def saludar(self, aQuien = 'amigo'):
        # super(Alumno, self).saludar(aQuien)
        Persona.saludar(self, aQuien)
        print(f'Y estudio {self.__curso}')


p1 = Persona('Pepe', 'pp@sample.com', 32)
a1 = Alumno('Ernesto', 'er@sample.com', 23, 'Python')
a1.saludar(p1.getNombre())