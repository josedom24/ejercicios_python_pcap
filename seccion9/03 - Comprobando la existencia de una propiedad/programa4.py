class ClaseEjemplo:
    a = 1  # Atributo de clase

    def __init__(self):
        self.b = 2  # Atributo de instancia

objeto = ClaseEjemplo()

print(hasattr(objeto, 'b'))  # Verifica si la instancia tiene el atributo 'b'
print(hasattr(objeto, 'a'))  # Verifica si la instancia tiene acceso al atributo de clase 'a'
print(hasattr(ClaseEjemplo, 'b'))    # Verifica si la clase tiene el atributo 'b'
print(hasattr(ClaseEjemplo, 'a'))    # Verifica si la clase tiene el atributo de clase 'a'
