from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def comunicarse(self):
        pass

class Perro(Animal):
    def __init__(self, nombre):
        Animal.__init__(self, nombre)

    def comunicarse(self):
       print(f'Guau, guau, me llamo {self.nombre} ')

class Gato(Animal):
    def __init__(self, nombre):
        Animal.__init__(self, nombre)

    def comunicarse(self):
        print(f'Miau, miau, me llamo {self.nombre} ')

p1 = Perro('Rufo')
p1.comunicarse()

g1 = Gato('Cesar')
g1.comunicarse()