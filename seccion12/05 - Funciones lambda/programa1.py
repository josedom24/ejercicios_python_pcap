dos = lambda: 2
raiz_cuadrada = lambda x: x * x
potencia = lambda x, y: x ** y

for a in range(-2, 3):
    print(raiz_cuadrada(a), end=" ")
    print(potencia(a, dos()))
