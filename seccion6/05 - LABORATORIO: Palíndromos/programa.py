texto = input("Ingresa un texto: ")

# Quitar todos los espacios...
texto = texto.replace(' ','')

# ... y revisar si la palabra es igual en ambos sentidos
if len(texto) > 1 and texto.upper() == texto[::-1].upper():
	print("Es un palíndromo")
else:
	print("No es un palíndromo")