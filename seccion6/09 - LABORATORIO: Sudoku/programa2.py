# Una función que verifica si una lista pasada como argumento contiene
# nueve dígitos del '1' al '9'.
def checkset(digitos):
    return sorted(list(digitos)) == [chr(x + ord('0')) for x in range(1, 10)]


sudoku1='''
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
'''

sudoku2='''
195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671
'''

# Una lista de filas que representan el Sudoku.
filas = [ ]
for r in range(9):
    ok = False
    while not ok:
        fila = sudoku1.split()[r]
        ok = len(fila) == 9 or fila.isdigit()
        if not ok:
            print("Datos de fila incorrectos: se requieren 9 dígitos")
    filas.append(fila)

ok = True

# Comprobar si todas las filas son correctas.
for r in range(9):
    if not checkset(filas[r]):
        ok = False
        break

# Comprobar si todas las columnas son correctas.	
if ok:
    for c in range(9):
        columnas = []
        for f in range(9):
            columnas.append(filas[f][c])
        if not checkset(columnas):
            ok = False
            break

# Comprobar si todos los subcuadrados (3x3) son correctos.
if ok:
    for f in range(0, 9, 3):
        for c in range(0, 9, 3):
            cuadro = ''
            # Hacer una cadena que contenga todos los dígitos de un subcuadrado.
            for i in range(3):
                cuadro += filas[f+i][c:c+3]
            if not checkset(list(cuadro)):
                ok = False
                break

# Imprimir el veredicto final.
if ok:
    print("Si")
else:
    print("No")