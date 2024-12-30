class ClaseSuper:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return "Mi nombre es " + self.nombre + "."


class SubClase(ClaseSuper):
    def __init__(self, nombre):
        super().__init__(nombre)


objeto = SubClase("Andy")
print(objeto)
