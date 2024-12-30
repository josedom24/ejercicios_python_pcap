# Probando propiedades: variables de clase.
class SuperClase:
    supVar = 1


class SubClase(SuperClase):
    subVar = 2


objeto = SubClase()
print(objeto.subVar)
print(objeto.supVar)
