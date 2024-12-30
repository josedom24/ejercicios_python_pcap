class ClaseSuper:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."


class SubClase(ClaseSuper):
    def __init__(self, nombre):
        ClaseSuper.__init__(self, nombre)


objeto = SubClase("Andy")
print(objeto)
