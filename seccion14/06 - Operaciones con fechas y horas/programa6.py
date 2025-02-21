from datetime import timedelta, date, datetime

# Otra operación útil es la suma de un objeto timedelta con un objeto date o datetime. 
# Esto permite ajustar fechas o momentos en el tiempo añadiendo días, horas, minutos o semanas.

# Crear un objeto timedelta
delta = timedelta(weeks=2, days=2, hours=2)

# Crear un objeto date y sumarle el timedelta
d = date(2019, 10, 4) + delta
print(d)

# Crear un objeto datetime y sumarle el timedelta
dt = datetime(2019, 10, 4, 14, 53) + delta
print(dt)
