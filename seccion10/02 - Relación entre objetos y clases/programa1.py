class Vehiculo:
    pass

class VehiculoTerrestre(Vehiculo):
    pass

class VehiculoOruga(VehiculoTerrestre):
    pass

mivehiculo = Vehiculo()
mivehiculoterrestre = VehiculoTerrestre()
mivehiculooruga = VehiculoOruga()

for obj in [mivehiculo, mivehiculoterrestre, mivehiculooruga]:
    for cls in [Vehiculo, VehiculoTerrestre, VehiculoOruga]:
        print(isinstance(obj, cls), end="\t")
    print()
