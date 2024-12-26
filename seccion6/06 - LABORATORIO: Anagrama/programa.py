cadena1 = input("Ingresa la primera cadena: ")
cadena2 = input("Ingresa la segunda cadena: ")

letras1 = ''.join(sorted(list(cadena1.upper().replace(' ',''))))
letras2 = ''.join(sorted(list(cadena2.upper().replace(' ',''))))
if len(letras1) > 0 and letras1 == letras2:
	print("Anagramas")
else:
	print("No son anagramas")