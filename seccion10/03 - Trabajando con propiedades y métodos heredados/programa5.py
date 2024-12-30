class Nivel1:
    variable_1 = 100
    def __init__(self):
        self.var_1 = 101

    def fun_1(self):
        return 102


class Nivel2(Nivel1):
    variable_2 = 200
    def __init__(self):
        super().__init__()
        self.var_2 = 201
    
    def fun_2(self):
        return 202


class Nivel3(Nivel2):
    variable_3 = 300
    def __init__(self):
        super().__init__()
        self.var_3 = 301

    def fun_3(self):
        return 302


objeto = Nivel3()

print(objeto.variable_1, objeto.var_1, objeto.fun_1())
print(objeto.variable_2, objeto.var_2, objeto.fun_2())
print(objeto.variable_3, objeto.var_3, objeto.fun_3())
