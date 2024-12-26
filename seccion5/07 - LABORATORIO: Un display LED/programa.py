digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]


def print_number(numero):
	global digits
	digitos = str(numero)
	lineas = [ '' for lin in range(5) ]
	for digito in digitos:
		segmentos = [ [' ',' ',' '] for lin in range(5) ]
		patron = digits[int(digito)]
		if patron[0] == '1':
			segmentos[0][0] = segmentos[0][1] = segmentos[0][2] = '#'
		if patron[1] == '1':
			segmentos[0][2] = segmentos[1][2] = segmentos[2][2] = '#'
		if patron[2] == '1':
			segmentos[2][2] = segmentos[3][2] = segmentos[4][2] = '#'
		if patron[3] == '1':
			segmentos[4][0] = segmentos[4][1] = segmentos[4][2] = '#'
		if patron[4] == '1':
			segmentos[2][0] = segmentos[3][0] = segmentos[4][0] = '#'
		if patron[5] == '1':
			segmentos[0][0] = segmentos[1][0] = segmentos[2][0] = '#'
		if patron[6] == '1':
			segmentos[2][0] = segmentos[2][1] = segmentos[2][2] = '#'
		for linea in range(5):
			lineas[linea] += ''.join(segmentos[linea]) + ' '
	for linea in lineas:
		print(linea)


print_number(int(input("Ingresa el número que deseas mostrar: ")))