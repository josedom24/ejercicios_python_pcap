from datetime import datetime

# Convertir cadena a objeto datetime usando strptime
fecha_hora = datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")
print(fecha_hora)

