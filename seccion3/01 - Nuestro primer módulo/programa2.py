from sys import path

path.append('modulos')  # Añade la carpeta 'modulos' a sys.path

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))   # Salida: 0
print(module.prodl(ones))    # Salida: 1
