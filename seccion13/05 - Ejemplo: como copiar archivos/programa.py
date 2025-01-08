from os import strerror

# Solicita al usuario el nombre del archivo fuente
source_file_name = input("Ingresa el nombre del archivo fuente: ")

# Intenta abrir el archivo fuente
try:
    source_file = open(source_file_name, 'rb')
except IOError as e:
    print("No se puede abrir el archivo fuente:", strerror(e.errno))
    exit(e.errno)

# Solicita al usuario el nombre del archivo destino
destination_file_name = input("Ingresa el nombre del archivo destino: ")

# Intenta abrir el archivo destino
try:
    destination_file = open(destination_file_name, 'wb')
except IOError as e:
    print("No se puede crear el archivo de destino:", strerror(e.errno))
    source_file.close()
    exit(e.errno)

# Prepara un búfer de 64 kilobytes
buffer = bytearray(65536)
total = 0

# Copia los datos del archivo fuente al archivo destino
try:
    readin = source_file.readinto(buffer)
    while readin > 0:
        written = destination_file.write(buffer[:readin])
        total += written
        readin = source_file.readinto(buffer)
except IOError as e:
    print("Error durante la copia:", strerror(e.errno))
    exit(e.errno)

# Imprime el número total de bytes escritos
print(total, 'byte(s) escritos con éxito')

# Cierra los archivos
source_file.close()
destination_file.close()
