class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objeto = ClaseEjemplo(1)

print(objeto.a)
print(objeto.b)
