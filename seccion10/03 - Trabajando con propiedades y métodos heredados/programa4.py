# Probando propiedades: variables de instancia.
class SuperClase:
    def __init__(self):
        self.supVar = 11


class SubClase(SuperClase):
    def __init__(self):
        super().__init__()
        self.subVar = 12


objeto = SubClase()
print(objeto.subVar)
print(objeto.supVar)
