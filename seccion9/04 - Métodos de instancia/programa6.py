class Clase:
    def __init__(self, value = None):
        self.var = value


objeto_1 = Clase("objeto")
objeto_2 = Clase()

print(objeto_1.var)
print(objeto_2.var)
