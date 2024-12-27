try:
    y = 1 / 0
except ZeroDivisionError:
    print("Uuuppsss...")

print("FIN.")

try:
    y = 1 / 0
except ArithmeticError:
    print("Uuuppsss...")

print("FIN.")