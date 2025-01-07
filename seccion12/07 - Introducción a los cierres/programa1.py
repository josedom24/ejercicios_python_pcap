def externa(par):
    loc = par

    def interna():
        return loc

    return interna

var = 1
fun = externa(var)
print(fun())
