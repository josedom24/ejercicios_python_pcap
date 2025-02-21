from datetime import timedelta

#El constructor de timedelta acepta los siguientes argumentos opcionales:
#
#    days: Número de días.
#    seconds: Número de segundos.
#    microseconds: Número de microsegundos.
#    milliseconds: Número de milisegundos.
#    minutes: Número de minutos.
#    hours: Número de horas.
#    weeks: Número de semanas.


# Crear un objeto timedelta con 2 semanas, 2 días y 3 horas
delta = timedelta(weeks=2, days=2, hours=3)
print(delta)

