class ClaseEjemplo:
    def __init__(self, val=1):
        self.__propiedad1 = val

    def crear_nueva_propiedad(self, val=2):
        self.__propiedad2 = val

objeto1 = ClaseEjemplo()

objeto2 = ClaseEjemplo(2)
objeto2.crear_nueva_propiedad(3)

objeto3 = ClaseEjemplo(4)
objeto3.__propiedad3 = 5

print(objeto1.__dict__)
print(objeto2.__dict__)
print(objeto3.__dict__)