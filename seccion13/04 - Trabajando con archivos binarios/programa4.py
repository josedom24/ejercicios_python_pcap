from os import strerror

data = bytearray(10)  # Crea un bytearray con espacio para 10 bytes

try:
    # Abre el archivo en modo binario para lectura
    binary_file = open('file.bin', 'rb')
    num_bytes_read = binary_file.readinto(data)  # Llena el bytearray con datos
    binary_file.close()  # Cierra el archivo

    # Imprime los valores leídos en formato hexadecimal
    for b in data:
        print(hex(b), end=' ')
except IOError as e:
    print("Se produjo un error de E/S:", strerror(e.errno))
