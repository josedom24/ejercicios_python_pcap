palabra = input("Ingresa la palabra que deseas encontrar: ").upper()
busqueda = input("Ingresa la cadena en donde deseas buscar: ").upper()

encontrado = True
indice = 0

for caracter in palabra:
	pos = busqueda.find(caracter, indice) 
	if pos < 0:
		encontrado = False
		break
	indice = pos + 1
if encontrado:
	print("Si")
else:
	print("No")
	   