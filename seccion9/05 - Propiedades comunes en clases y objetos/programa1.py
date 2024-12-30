class Clase:
    varia = 1
    def __init__(self):
        self.var = 2

    def metodo(self):
        pass

    def __oculto(self):
        pass


objeto = Clase()

print(objeto.__dict__)
print(Clase.__dict__)
