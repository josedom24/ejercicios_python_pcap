# Ingresa el texto a encriptar.
texto = input("Ingresa un mensaje: ")

# Ingresar un valor de cambio válido (repitelo hasta que tengas éxito).
desplazamiento = 0

while desplazamiento == 0:
    try:    
        desplazamiento = int(input("Ingresa el valor de cambio del cifrado (1..25): "))
        if desplazamiento not in range(1,26):
        	raise ValueError
    except ValueError:
        desplazamiento = 0
    if desplazamiento == 0:
        print("¡Valor de cambio inválido!")

cifrado = ''

for caracter in texto:
    # ¿Es un letra?
    if caracter.isalpha():
        # Cambia su código.
        code = ord(caracter) + desplazamiento
        # Encontrar el código de la primera letra (mayúscula o minúscula).
        if caracter.isupper():
            primera_letra = ord('A')
        else:
            primera_letra = ord('a')
        # Realizar corrección.
        code -= primera_letra
        code %= 26
        # Agregar carácter codificado al mensaje.
        cifrado += chr(primera_letra + code)
    else:
        # Agregar carácter original al mensaje.
        cifrado += caracter

print(cifrado)