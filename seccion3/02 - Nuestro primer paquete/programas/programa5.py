from sys import path

path.append('../paquetes')

import ciencia.plantas.arboles as arboles
import ciencia.plantas.flores as flores

print(arboles.Crecer())
print(flores.Florecer())
