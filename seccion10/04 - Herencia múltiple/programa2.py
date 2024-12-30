class Nivel1:
    var = 100
    def fun(self):
        return 101

class Nivel2(Nivel1):
    var = 200
    def fun(self):
        return 201

class Nivel3(Nivel2):
    pass

objeto = Nivel3()

print(objeto.var, objeto.fun())  # Salida: 200 201
