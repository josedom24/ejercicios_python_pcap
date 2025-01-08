from datetime import date

d = date(1991, 2, 5)
print(d)  # Imprime: 1991-02-05

d = d.replace(year=1992, month=1, day=16)
print(d)  # Imprime: 1992-01-16
