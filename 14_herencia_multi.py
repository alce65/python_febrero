class Ciudadano():
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print('Soy un ciudadano')

class Estudiante():
    def __init__(self, curso):
        self.curso = curso
    def saludar(self):
        print('Soy un estudiante')

class Usuario(Ciudadano, Estudiante):
    def __init__(self, nombre, curso, clave):
        Ciudadano.__init__(self, nombre)
        Estudiante.__init__(self, curso)
        self.clave = clave
    def __str__(self):
        return f'Soy {self.nombre}, estudio {self.curso} y mi clave es ({self.clave})'

    # Polimordfismo    
    # def saludar(self):
    #     Ciudadano.saludar(self)
    #     Estudiante.saludar(self)

user1 = Usuario('Pepe', 'Phyton', '1234')
print(user1)
user1.saludar()
