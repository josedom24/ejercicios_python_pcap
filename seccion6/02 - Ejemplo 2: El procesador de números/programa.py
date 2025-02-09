#Procesador de Números.

linea = input("Ingresa una línea de números, sepáralos con espacios: ")
cadenas = linea.split()
total = 0
try:
    for car_num in cadenas:
        total += float(car_num)
    print("El total es:", total)
except:
    print(car_num, "no es un numero.")
