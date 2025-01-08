# Crear un bytearray de 10 bytes
data = bytearray(10)
print(data)  # Salida: bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Modificar un byte
data[0] = 65  # Cambiar el primer byte a 65 (corresponde a 'A')
print(data)  # Salida: bytearray(b'A\x00\x00\x00\x00\x00\x00\x00\x00\x00')

# Agregar nuevos bytes
data.append(66)  # Agregar 66 (corresponde a 'B')
print(data)  # Salida: bytearray(b'A\x00\x00\x00\x00\x00\x00\x00\x00\x00B')

# Convertir a bytes
bytes_data = bytes(data)
print(bytes_data)  # Salida: b'A\x00\x00\x00\x00\x00\x00\x00\x00\x00B'
