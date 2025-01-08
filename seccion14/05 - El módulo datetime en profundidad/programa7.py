import time

# Convertir cadena a objeto struct_time usando strptime
fecha_hora_struct = time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")
print(fecha_hora_struct)
