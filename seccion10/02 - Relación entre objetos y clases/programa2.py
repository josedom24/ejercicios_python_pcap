class ClaseEjemplo:
    def __init__(self, val):
        self.val = val

objeto1 = ClaseEjemplo(0)
objeto2 = ClaseEjemplo(2)
objeto3 = objeto1
objeto3.val += 1

print(objeto1 is objeto2)  # Comparando objeto1 y objeto2
print(objeto2 is objeto3)  # Comparando objeto2 y objeto3
print(objeto3 is objeto1)  # Comparando objeto3 y objeto1
print(objeto1.val, objeto2.val, objeto3.val)

string_1 = "Mary tenía un "
string_2 = "Mary tenía un corderito"
string_1 += "corderito"

print(string_1 == string_2, string_1 is string_2)  # Comparación de cadenas
