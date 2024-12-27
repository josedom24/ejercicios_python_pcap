lista = [1, 2, 3, 4, 5]
indice = 0
continua = True

while continua:
    try:
        print(lista[indice])
        indice += 1
    except IndexError:
        continua = False
print('Listo')