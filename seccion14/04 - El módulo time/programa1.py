from datetime import time

# El constructor de la clase time acepta los siguientes parámetros:
#
#    hour: (0-23) Hora del día.
#    minute: (0-59) Minuto de la hora.
#    second: (0-59) Segundo del minuto.
#    microsecond: (0-999999) Microsegundo del segundo.
#    tzinfo: (opcional) Un objeto de la subclase tzinfo que proporciona información sobre la zona horaria, o None (por defecto).
#    fold: (opcional) Debe ser 0 o 1, con un valor predeterminado de 0, que se utiliza para representar ambigüedades en los cambios de hora.


# Creando un objeto de tipo time
t = time(14, 53, 20, 1)

# Mostrando el tiempo y sus componentes
print("Tiempo:", t)                      # Salida: Tiempo: 14:53:20.000001
print("Hora:", t.hour)                   # Salida: Hora: 14
print("Minuto:", t.minute)               # Salida: Minuto: 53
print("Segundo:", t.second)               # Salida: Segundo: 20
print("Microsegundo:", t.microsecond)     # Salida: Microsegundo: 1
