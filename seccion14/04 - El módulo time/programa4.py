import time

# gmtime() y localtime() son útiles para convertir un valor de tiempo en segundos 
# a un objeto struct_time, que descompone el tiempo en componentes legibles como año, mes, día, etc.

#time.struct_time:
#    tm_year   # Año (por ejemplo, 2024)
#    tm_mon    # Mes (1 a 12)
#    tm_mday   # Día del mes (1 a 31)
#    tm_hour   # Hora (0 a 23)
#    tm_min    # Minuto (0 a 59)
#    tm_sec    # Segundo (0 a 61)
#    tm_wday   # Día de la semana (0 = Lunes, 6 = Domingo)
#    tm_yday   # Día del año (1 a 366)
#    tm_isdst  # Horario de verano (1: sí, 0: no, -1: desconocido)
#    tm_zone   # Nombre de la zona horaria (abreviado)
#    tm_gmtoff # Desplazamiento UTC en segundos

# Timestamp específico
timestamp = 1572879180

# Convertir a UTC Tiempo Universal Coordinad
utc_time = time.gmtime(timestamp)
print(utc_time)

# Convertir a hora local
local_time = time.localtime(timestamp)
print(local_time)
