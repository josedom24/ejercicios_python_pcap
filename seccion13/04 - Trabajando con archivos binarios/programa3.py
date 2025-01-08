from os import strerror

# Inicializa el bytearray
data = bytearray(10)

# Llena el bytearray con valores
for i in range(len(data)):
    data[i] = 10 + i  # Valores de 10 a 19

try:
    # Abre el archivo en modo binario para escritura
    binary_file = open('file.bin', 'wb')
    binary_file.write(data)  # Escribe el bytearray en el archivo
    binary_file.close()  # Cierra el archivo
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
