class ClaseEjemplo:
    contador = 0  # Variable de clase

    def __init__(self, val=1):
        self.__propiedad1 = val
        ClaseEjemplo.contador += 1  # Incrementa el contador en cada instancia creada

objeto1 = ClaseEjemplo()
objeto2 = ClaseEjemplo(2)
objeto3 = ClaseEjemplo(4)

print(objeto1.__dict__, objeto1.contador)
print(objeto2.__dict__, objeto2.contador)
print(objeto3.__dict__, objeto3.contador)
