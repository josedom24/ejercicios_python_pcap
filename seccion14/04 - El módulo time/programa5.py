import time

# Timestamp específico
timestamp = 1572879180

# Obtener struct_time en UTC
st = time.gmtime(timestamp)

# Convertir struct_time a cadena legible
print(time.asctime(st))

# Convertir tupla a timestamp
timestamp_from_tuple = time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))
print(timestamp_from_tuple)
