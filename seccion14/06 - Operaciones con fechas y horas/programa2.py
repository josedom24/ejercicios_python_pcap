from datetime import date
from datetime import timedelta

# Una vez que se obtiene un objeto timedelta, se pueden realizar varias operaciones como sumar o restar días, horas, minutos, etc
# Crear un objeto timedelta
delta = timedelta(days=5, hours=2, minutes=30)

# Sumar timedelta a una fecha
d1 = date(2020, 11, 4)
nueva_fecha = d1 + delta
print(nueva_fecha)
