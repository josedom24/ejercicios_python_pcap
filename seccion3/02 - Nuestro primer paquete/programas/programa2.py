from sys import path

path.append('modulos')  # Añade la carpeta 'modulos' a sys.path

import module

ceros = [0 for i in range(5)]
unos = [1 for i in range(5)]
print(module.suma(ceros))  # Salida: 0
print(module.producto(unos))   # Salida: 1
