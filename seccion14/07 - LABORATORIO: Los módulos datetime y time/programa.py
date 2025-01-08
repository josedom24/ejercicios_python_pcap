from datetime import datetime

mifecha = datetime(2020, 11, 4, 14, 53)

print(mifecha.strftime("%Y/%m/%d %H:%M:%S"))
print(mifecha.strftime("%y/%B/%d %H:%M:%S %p"))
print(mifecha.strftime("%a, %Y %b %d"))
print(mifecha.strftime("%A, %Y %B %d"))
print(mifecha.strftime("Día de la semana: %w"))
print(mifecha.strftime("Día del año: %j"))
print(mifecha.strftime("Número de semana en el año: %W"))