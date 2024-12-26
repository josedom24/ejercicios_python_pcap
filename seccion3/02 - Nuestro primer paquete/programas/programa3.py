from sys import path
path.append('../paquetes')

import ciencia.clima
import ciencia.animales.aves

print(ciencia.clima.Predecir())
print(ciencia.animales.aves.Volar())

from ciencia.clima import Predecir
print(Predecir())
