from datetime import date

# date: Representa una fecha (año, mes y día).
# date.today: Fecha actual

today = date.today()

print("Hoy:", today)
print("Año:", today.year)
print("Mes:", today.month)
print("Día:", today.day)

# Crear un objeto date
# A partir del año, mes y día

my_date = date(2019, 11, 4)
print(my_date)

# A partir de una marca de tiempo (segundos transcurridos desde el 1 de enero de 1970).

import time

timestamp = time.time()
print("Marca de tiempo:", timestamp)

d = date.fromtimestamp(timestamp)
print("Fecha:", d)

# A partir de una fecha en formato ISO

d = date.fromisoformat('2019-11-04')
print(d)

# Modificación de una fecha

d = date(1991, 2, 5)
print(d)  # Imprime: 1991-02-05

d = d.replace(year=1992, month=1, day=16)
print(d)  # Imprime: 1992-01-16

# Calcular el día de la semana

d = date(2019, 11, 4)  # 4 de noviembre de 2019
print(d.weekday())      # Salida: 0 (Lunes)

print(d.isoweekday())   # Salida: 1 (Lunes)