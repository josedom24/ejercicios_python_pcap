from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)  # Convierte 90 grados a radianes
ad = degrees(ar)  # Convierte nuevamente a grados

print(ad == 90.)  # Verifica si el valor en grados sigue siendo 90
print(ar == pi / 2.)  # Verifica si el valor en radianes es pi/2
print(sin(ar) / cos(ar) == tan(ar))  # Verifica si la tangente es sin/cos
print(asin(sin(ar)) == ar)  # Verifica si el arcoseno de sin(pi/2) devuelve pi/2
