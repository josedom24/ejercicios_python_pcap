import calendar

# Verificar el día de la semana para el 24 de diciembre de 2020
print(calendar.weekday(2020, 12, 24))

# Obtener encabezados semanales con un ancho de 2 caracteres
print(calendar.weekheader(2))

# Comprobar si 2020 es un año bisiesto
print(calendar.isleap(2020))

# Contar años bisiestos entre 2010 y 2021 (sin incluir 2021)
print(calendar.leapdays(2010, 2021))

