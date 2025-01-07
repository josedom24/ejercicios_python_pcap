def cierre(par):
    loc = par

    def potencia(p):
        return p ** loc
    return potencia

fsqr = cierre(2)  # Cierre que eleva al cuadrado
fcub = cierre(3)  # Cierre que eleva al cubo

for i in range(5):
    print(i, fsqr(i), fcub(i))
