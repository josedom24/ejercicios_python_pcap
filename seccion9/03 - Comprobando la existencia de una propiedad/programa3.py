class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objeto = ClaseEjemplo(1)

# Acceso seguro usando hasattr
print(objeto.a)

if hasattr(objeto, 'b'):
    print(objeto.b)
else:
    print("El atributo 'b' no existe.")
