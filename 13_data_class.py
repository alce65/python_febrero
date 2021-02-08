from dataclasses import dataclass

@dataclass
class Libro:
        titulo : str
        autor : str
        año : int
    

b1 = Libro('Señor de los Anillos', 'J.R.R. Tolkien', 1954)

print(b1)
print(str(b1))
print(repr(b1))