class Estrella:
    def __init__(self, nombre, galaxia):
        self.nombre = nombre
        self.galaxia = galaxia

    def __str__(self):
        return self.nombre + ' en ' + self.galaxia

    
sol = Estrella("Sol", "Vía Láctea")
print(sol)          # Invoca __str__()
