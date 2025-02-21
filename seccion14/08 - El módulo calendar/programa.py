import calendar

# Días de la semana

# En el módulo calendar, los días de la semana se representan con valores enteros de la siguiente manera:
# Día de la semana 	Valor entero 	Constante
# Lunes 	    0 	calendar.MONDAY
# Martes 	    1 	calendar.TUESDAY
# Miércoles 	2 	calendar.WEDNESDAY
# Jueves 	    3 	calendar.THURSDAY
# Viernes 	4 	calendar.FRIDAY
# Sábado 	    5 	calendar.SATURDAY
# Domingo 	6 	calendar.SUNDAY

# Los meses se empiezan a contar desde 1

# Visualización de calendarios
print(calendar.calendar(2020))

#Si deseas ajustar el formato del calendario, puedes utilizar los siguientes parámetros opcionales:
#
#    w: Establece el ancho de la columna de fecha (por defecto es 2).
#    l: Define el número de líneas por semana (por defecto es 1).
#    c: Especifica el número de espacios entre las columnas del mes (por defecto es 6).
#    m: Define el número de columnas (por defecto es 3).

# Una alternativa a la función calendar es la función prcal. 
# Esta función también permite mostrar el calendario de un año, pero no requiere el uso de print para mostrar el resultado.

calendar.prcal(2020)

# Calendario para un mes específico
print(calendar.month(2020, 11))
calendar.prmonth(2020, 11)

# puedes personalizar el formato de la función month utilizando los siguientes parámetros opcionales:
# 
#     w: Ancho de la columna de fecha (el valor predeterminado es 2).
#     l: Número de líneas por semana (el valor predeterminado es 1).

# Configurar el primer día de la semana

# Cambiar el primer día de la semana a domingo
calendar.setfirstweekday(calendar.SUNDAY)

# Imprimir el calendario de diciembre de 2020
calendar.prmonth(2020, 12)


# Verificar el día de la semana para el 24 de diciembre de 2020
print(calendar.weekday(2020, 12, 24))

# Obtener encabezados semanales con un ancho de 2 caracteres
print(calendar.weekheader(2))

# Comprobar si 2020 es un año bisiesto
print(calendar.isleap(2020))

# Contar años bisiestos entre 2010 y 2021 (sin incluir 2021)
print(calendar.leapdays(2010, 2021))