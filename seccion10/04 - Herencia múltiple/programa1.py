class SuperA:
    var_a = 10
    def fun_a(self):
        return 11

class SuperB:
    var_b = 20
    def fun_b(self):
        return 21

class Sub(SuperA, SuperB):
    pass

objeto = Sub()

print(objeto.var_a, objeto.fun_a())  # Salida: 10 11
print(objeto.var_b, objeto.fun_b())  # Salida: 20 21
