from math import tan, radians
angle = int(input('Ingresa un ángulo entero en grados: '))
# Asegúrate de que angle != 90 + k * 180
assert angle % 180 != 90
print(tan(radians(angle)))