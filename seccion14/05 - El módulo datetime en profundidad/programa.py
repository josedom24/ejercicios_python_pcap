from datetime import date
from datetime import time
from datetime import datetime


# Al crear un objeto datetime, se deben proporcionar los siguientes parámetros:
# 
#     year: El año debe estar en el rango de 1 a 9999.
#     month: El mes debe ser un valor entre 1 y 12.
#     day: El día debe estar comprendido entre 1 y el último día del mes correspondiente.
#     hour: La hora debe estar entre 0 y 23.
#     minute: El minuto debe estar entre 0 y 59.
#     second: El segundo debe estar entre 0 y 59.
#     microsecond: Los microsegundos deben estar entre 0 y 999999.
#     tzinfo: Este parámetro define la zona horaria y puede ser una subclase de tzinfo o None.
#     fold: Un valor opcional que puede ser 0 o 1, utilizado para distinguir momentos ambiguos durante los cambios de horario (por defecto es 0).
# 

dt = datetime(2019, 11, 4, 14, 53)

print("Fecha y Hora:", dt)
print("Fecha:", dt.date())
print("Hora:", dt.time())

# Métodos que devuelven la fecha y hora actuales

# today(): devuelve la fecha y hora local actual con el atributo tzinfo establecido a None.
# now(): devuelve la fecha y hora local actual igual que el método today(), a menos que le pasemos el argumento opcional tz. 
# utcnow(): devuelve la fecha y hora UTC actual con el atributo tzinfo establecido a None.

print("hoy:", datetime.today())
print("ahora:", datetime.now())
print("utc_ahora:", datetime.utcnow())

# Obtener marca de tiempo

dt = datetime(2020, 10, 4, 14, 55)
print("Marca de tiempo:", dt.timestamp())

# Formato de fecha
# Método strftime()

    # %Y: Representa el año con el siglo, como un número decimal (por ejemplo, 2020).
    # %m: Representa el mes como un número decimal con relleno de ceros si es necesario (por ejemplo, 01 para enero).
    # %d: Representa el día del mes como un número decimal con relleno de ceros (por ejemplo, 04).

# Formato de hora
#    %H: Representa la hora en formato de 24 horas (con relleno de ceros si es necesario).
#    %M: Representa los minutos como un número decimal con relleno de ceros.
#    %S: Representa los segundos como un número decimal con relleno de ceros.

# Formato combinado de fecha y hora

#    %y: Representa el año en dos dígitos (por ejemplo, 20 para 2020).
#    %B: Representa el nombre completo del mes (por ejemplo, "November").
#    %d: Representa el día del mes como un número decimal con relleno de ceros.

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

# La función strftime() en el módulo time

import time

timestamp = 1572879180  # Ejemplo de marca de tiempo
st = time.gmtime(timestamp)

# Formatear usando un objeto struct_time
print(time.strftime("%Y/%m/%d %H:%M:%S", st))

# Formatear la hora local actual
print(time.strftime("%Y/%m/%d %H:%M:%S"))

# El método strptime()
# convierte una cadena que representa una fecha y hora en un objeto datetime

fecha_hora_struct = time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S")
print(fecha_hora_struct)