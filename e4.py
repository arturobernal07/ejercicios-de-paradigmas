class Rectangulo:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def area(self):
        return self.ancho * self.alto

    def perimetro(self):
        return 2 * (self.ancho + self.alto)


r = Rectangulo(5, 3)
print("Área:", r.area())        
print("Perímetro:", r.perimetro())