## try:
##     # Código que puede fallar
## except:
##     # Código que maneja el fallo

try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh cielos, algo salió mal...")

print("3")