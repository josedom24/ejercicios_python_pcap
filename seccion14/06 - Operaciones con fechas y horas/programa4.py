from datetime import timedelta

# Crear un objeto timedelta
delta = timedelta(weeks=2, days=2, hours=3)
print("Días:", delta.days)            # Devuelve 16 días
print("Segundos:", delta.seconds)      # Devuelve 10800 segundos (3 horas convertidas a segundos)
print("Microsegundos:", delta.microseconds)  # Devuelve 0
