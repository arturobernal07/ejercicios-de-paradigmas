class AgendaContacto:
    def __init__(self):
        self.contactos = {}

    def agregar(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def buscar(self, nombre):
        if nombre in self.contactos:
            return self.contactos[nombre]
        return "No existe"

ag = AgendaContacto()
ag.agregar("arturo", "266-040-5458")
print(ag.buscar("esme")) 
print(ag.buscar("Miri"))
