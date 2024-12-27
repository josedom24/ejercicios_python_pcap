diccionario = {'a': 'b', 'b': 'c', 'c': 'd'}
clave = 'a'

try:
    while True:
        clave = diccionario[clave]
        print(clave)
except KeyError:
    print('No existe tal clave:', clave)
