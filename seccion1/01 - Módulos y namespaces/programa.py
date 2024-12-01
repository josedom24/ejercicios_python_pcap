import math

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

pi = 3.14

print(sin(pi/2))        # Usará tu propia definición de sin y pi.
print(math.sin(math.pi/2))  # Usará la función sin y pi del módulo math.
