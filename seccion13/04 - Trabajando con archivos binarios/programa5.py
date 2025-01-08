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

# Ingresa aquí el código que lee los bytes del stream.
try:
    # Abre el archivo en modo binario para lectura
    binary_file = open('file.bin', 'rb')
    
    # Lee todo el contenido del archivo en un objeto de bytes
    data = binary_file.read()
    binary_file.close()  # Cierra el archivo

    # Convierte el objeto de bytes a bytearray para manipulación
    byte_data = bytearray(data)

    # Imprime los valores leídos en formato hexadecimal
    for b in byte_data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
