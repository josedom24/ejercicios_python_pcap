from datetime import timedelta

# El objeto timedelta puede multiplicarse por un número entero.
# Esta operación multiplica todos los componentes del intervalo de tiempo, como los días y las horas.

# Crear un objeto timedelta con 16 días y 2 horas
delta = timedelta(weeks=2, days=2, hours=2)
print(delta)

# Multiplicar el timedelta por 2
delta2 = delta * 2
print(delta2)
