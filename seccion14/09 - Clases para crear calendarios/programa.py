import calendar

# Crear un objeto Calendar que comienza en Domingo
c = calendar.Calendar(calendar.SUNDAY)

# Iterar sobre los días de la semana y mostrar sus valores
for weekday in c.iterweekdays():
    print(weekday, end=" ")
print()
print(20*"-")
# Iterar sobre las fechas del mes de Noviembre de 2019
for date in c.itermonthdates(2019, 11):
    print(date, end=" ")
print()
print(20*"-")
# Iterar sobre los días del mes
for date in c.itermonthdays(2019, 11):
    print(date, end=" ")
print()
print(20*"-")
# Respresrntación estructurada
for data in c.monthdays2calendar(2020, 12):
    print(data)
