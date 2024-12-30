class ClaseEjemplo:
    __contador = 0
    def __init__(self, val = 1):
        self.__propiedad1 = val
        ClaseEjemplo.__contador += 1


objeto1 = ClaseEjemplo()
objeto2 = ClaseEjemplo(2)
objeto3 = ClaseEjemplo(4)

print(objeto1.__dict__, objeto1._ClaseEjemplo__contador)
print(objeto2.__dict__, objeto2._ClaseEjemplo__contador)
print(objeto3.__dict__, objeto3._ClaseEjemplo__contador)
