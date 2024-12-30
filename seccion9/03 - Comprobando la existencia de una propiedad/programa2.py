class ClaseEjemplo:
    def __init__(self, val):
        if val % 2 != 0:
            self.a = 1
        else:
            self.b = 1

objeto = ClaseEjemplo(1)

# Intento de acceso a atributo inexistente con manejo de excepciones
try:
    print(objeto.b)
except AttributeError:
	print("El atributo 'b' no existe.")
