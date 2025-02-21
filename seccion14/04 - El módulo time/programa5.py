import time

# asctime() convierte un objeto struct_time o una tupla que representa el tiempo en una cadena en un formato legible. 
# mktime() convierte un objeto struct_time o una tupla que expresa la hora local a una marca de tiempo.

#El formato de la tupla con la que vamos a trabajar tiene la siguiente estructura:
#
#    tm_year (año)
#    tm_mon (mes, 1-12)
#    tm_mday (día del mes, 1-31)
#    tm_hour (hora, 0-23)
#    tm_min (minuto, 0-59)
#    tm_sec (segundo, 0-59)
#    tm_wday (día de la semana, 0-6)
#    tm_yday (día del año, 1-366)
#    tm_isdst (horario de verano, 1: sí, 0: no, -1: desconocido)


# Timestamp específico
timestamp = 1572879180

# Obtener struct_time en UTC
st = time.gmtime(timestamp)

# Convertir struct_time a cadena legible
print(time.asctime(st))

# Convertir tupla a timestamp
timestamp_from_tuple = time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0))
print(timestamp_from_tuple)
