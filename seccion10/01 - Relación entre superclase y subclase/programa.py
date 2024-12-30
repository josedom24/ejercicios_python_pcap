class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass

for clase1 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
    for clase2 in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(issubclass(clase1, clase2), end="\t")
    print()
