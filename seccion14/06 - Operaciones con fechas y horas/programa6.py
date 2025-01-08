from datetime import timedelta, date, datetime

# Crear un objeto timedelta
delta = timedelta(weeks=2, days=2, hours=2)

# Crear un objeto date y sumarle el timedelta
d = date(2019, 10, 4) + delta
print(d)

# Crear un objeto datetime y sumarle el timedelta
dt = datetime(2019, 10, 4, 14, 53) + delta
print(dt)
