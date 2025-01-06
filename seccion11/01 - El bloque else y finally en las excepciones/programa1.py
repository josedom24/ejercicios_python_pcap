def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        return None
    else:
        print("Todo salió bien")
        return n

print(reciprocal(2))  # Salida esperada: "Todo salió bien" seguido de "0.5"
print(reciprocal(0))  # Salida esperada: "División fallida" seguido de "None"
