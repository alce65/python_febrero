class Persona():
    
    def __init__(self, nombre, correo, edad):
        self.__nombre = nombre
        self.__correo = correo
        self.__edad = edad

    def adoptaMascota (self, mascota):
        self.__mascota = mascota

    def mostrarMascota(self):
        #print(self.__mascota)
        print(f'''
           Tengo un {self.__mascota.especie()} 
           que se llama {self.__mascota.nombre()}
           ''') 

class Mascota():
    
    def __init__(self, especie, nombre):
        self.__especie = especie
        self.__nombre = nombre

    def especie(self, especie = None):
        if especie: self.__especie = especie
        return self.__especie

    def nombre(self, nombre = None):
        if nombre: self.__nombre = nombre
        return self.__nombre

    def __str__(self):
        return f'Soy un {self.especie()} y me llama "{self.nombre()}".'

p1 = Persona('Maria', 'ma@samle.es', 34)
p2 = Persona('Manuel', 'm@samle.es', 34)
m1 = Mascota('gato', 'Cesar')
p1.adoptaMascota(Mascota('perro', 'Rufus'))
p2.adoptaMascota(m1)
p1.mostrarMascota()
p2.mostrarMascota()