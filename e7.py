class Estudiante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.calificaciones = []

    def agregar_calificacion(self, valor):
        if 0 <= valor <= 10:
            self.calificaciones.append(valor)

    def promedio(self):
        if len(self.calificaciones) == 0:
            return 0
        return sum(self.calificaciones) / len(self.calificaciones)

al = Estudiante("Luis")
al.agregar_calificacion(9)
al.agregar_calificacion(8)
al.agregar_calificacion(10)
print("Promedio:", al.promedio())
