from sys import path

path.append('../paquetes')

import ciencia.animales.mamiferos.perro
from ciencia.animales.mamiferos.gato import Maullar

print(ciencia.animales.mamiferos.perro.Ladrar())
print(Maullar())
