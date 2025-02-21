from datetime import timedelta

# Internamente, los objetos timedelta almacenan el tiempo en días, segundos y microsegundos.
# Puedes acceder a estos valores directamente usando los atributos .days, .seconds y .microseconds.

# Crear un objeto timedelta
delta = timedelta(weeks=2, days=2, hours=3)
print("Días:", delta.days)            # Devuelve 16 días
print("Segundos:", delta.seconds)      # Devuelve 10800 segundos (3 horas convertidas a segundos)
print("Microsegundos:", delta.microseconds)  # Devuelve 0
