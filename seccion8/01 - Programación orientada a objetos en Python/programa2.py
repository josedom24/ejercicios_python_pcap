class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca  # Atributo
        self.modelo = modelo  # Atributo

    def describir(self):
        # Método que imprime una descripción del coche
        return "Coche: " + self.marca+ " " +self.modelo

class CocheElectrico(Coche):  # CocheElectrico hereda de Coche
    def __init__(self, marca, modelo, autonomia):
        super().__init__(marca, modelo)  # Llamar al constructor de la superclase
        self.autonomia = autonomia  # Atributo adicional

    def describir(self):
        # Método que incluye la autonomía en la descripción
        return "Coche eléctrico: "+ self.marca + " " + self.modelo +", Autonomía: " + str(self.autonomia) + " km"

# Crear un objeto de la clase CocheElectrico
mi_coche_electrico = CocheElectrico("Tesla", "Model S", 500)

# Usar el método del objeto
print(mi_coche_electrico.describir())  # Salida: Coche eléctrico: Tesla Model S, Autonomía: 500 km
