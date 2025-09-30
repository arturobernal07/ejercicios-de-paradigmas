class Circulo:
    PI = 3.1415926535

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return Circulo.PI * (self.radio ** 2)

    def circunferencia(self):
        return 2 * Circulo.PI * self.radio

c = Circulo(4)
print("Área:", c.area())              
print("Circunferencia:", c.circunferencia())
