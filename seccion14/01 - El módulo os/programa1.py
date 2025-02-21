import os

# os.uname devuelve un objeto con varios atributos

# systemname: almacena el nombre del sistema operativo.
# nodename: almacena el nombre de la máquina en la red.
# release: almacena la versión del sistema operativo.
# version: almacena detalles sobre la versión del sistema operativo.
# machine: almacena el identificador de hardware (por ejemplo, x86_64).

print(os.uname())

# os.name: identifica el sistema operativo.
print(os.name)
