class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo
        self.modelo = modelo  # Atributo

    def describir(self):
        # Método que imprime una descripción del coche
        return "Coche: " + self.marca+ " " +self.modelo

# Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla")

# Usar el método del objeto
print(mi_coche.describir())  # Salida: Coche: Toyota Corolla