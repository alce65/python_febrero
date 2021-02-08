class Libro:
    
    def __init__(self, titulo, autor, año):
        self.titulo = titulo
        self.autor = autor
        self.año = año
    
    def __str__(self):
        return f'{self.titulo} de {self.autor} ({self.año})'

    def __repr__(self):
        return str(dict(titulo=self.titulo, autor=self.autor,año=self.año))


b1 = Libro('Señor de los Anillos', 'J.R.R. Tolkien', 1954)

print(b1)
print(str(b1))
print(repr(b1))