class Left:
    var = "L"
    var_left = "LL"
    def fun(self):
        return "Left"

class Right:
    var = "R"
    var_right = "RR"
    def fun(self):
        return "Right"

class Sub(Left, Right):
    pass

objeto = Sub()

print(objeto.var, objeto.var_left, objeto.var_right, objeto.fun())  # Salida: L LL RR Left
