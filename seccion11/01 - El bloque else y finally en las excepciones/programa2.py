def reciprocal(n):
    try:
        n = 1 / n
    except ZeroDivisionError:
        print("División fallida")
        n = None
    else:
        print("Todo salió bien")
    finally:
        print("Es momento de decir adiós")
    return n

print(reciprocal(2))  # Salida esperada: "Todo salió bien", "Es momento de decir adiós", "0.5"
print(reciprocal(0))  # Salida esperada: "División fallida", "Es momento de decir adiós", "None"
