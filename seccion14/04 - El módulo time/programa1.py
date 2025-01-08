from datetime import time

# Creando un objeto de tipo time
t = time(14, 53, 20, 1)

# Mostrando el tiempo y sus componentes
print("Tiempo:", t)                      # Salida: Tiempo: 14:53:20.000001
print("Hora:", t.hour)                   # Salida: Hora: 14
print("Minuto:", t.minute)               # Salida: Minuto: 53
print("Segundo:", t.second)               # Salida: Segundo: 20
print("Microsegundo:", t.microsecond)     # Salida: Microsegundo: 1
