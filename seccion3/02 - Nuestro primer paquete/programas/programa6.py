from sys import path

path.append('../paquetes/cienciapack.zip')

import ciencia.plantas.arboles as arboles
import ciencia.plantas.flores as flores
from ciencia.animales.mamiferos.perro import Ladrar
from ciencia.animales.mamiferos.gato import Maullar
from ciencia.clima import Predecir

print(arboles.Crecer())
print(flores.Florecer())
print(Ladrar())
print(Maullar())
print(Predecir())
