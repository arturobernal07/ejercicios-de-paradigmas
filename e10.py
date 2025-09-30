class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return "Prestado"
        return "No disponible"

    def devolver(self):
        self.disponible = True

lb = Libro("Python Básico", "Algo")
print(lb.prestar())
print(lb.prestar()) 
lb.devolver()
print(lb.prestar())
