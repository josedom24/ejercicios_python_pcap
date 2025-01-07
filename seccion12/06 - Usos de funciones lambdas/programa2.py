def elevar_potencia(x):
    return 2 ** x

def cuadrado(x):
    return x * x

list_1 = [x for x in range(5)]
list_2 = list(map(elevar_potencia, list_1))
print(list_2)
for x in map(cuadrado, list_2):
    print(x, end=' ')
print()
