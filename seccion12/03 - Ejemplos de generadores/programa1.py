def potencia_de_2(n):
    resultado = 1
    for i in range(n):
        yield resultado
        resultado *= 2


for v in potencia_de_2(8):
    print(v)

t = [x for x in potencia_de_2(5)]
print(t)

t = list(potencia_de_2(3))
print(t)

for i in range(20):
    if i in potencia_de_2(4):
        print(i)
