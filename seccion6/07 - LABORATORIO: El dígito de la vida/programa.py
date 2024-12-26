fecha = input("Ingresa tu fecha de cumpleaños (en el siguiente formato: AAAAMMDD o AAAADDMM, 8 dígitos): ")
if len(fecha) != 8 or not fecha.isdigit():
    print("Formato de fecha inválida.")
else:
    while len(fecha) > 1:
        suma = 0
        for digito in fecha:
            suma += int(digito)
        print(fecha)
        fecha = str(suma)
    print("Tu Dígito de la Vida es: " + fecha)