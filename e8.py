class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def precio_con_descuento(self, porcentaje):
        if 0 <= porcentaje <= 100:
            return self.precio * (1 - porcentaje/100)
        return self.precio

p = Producto("lap", 30000)
print("Con 15%:", p.precio_con_descuento(15))
