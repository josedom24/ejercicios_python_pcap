# Demostración de la función list():
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Demonstrando el método find():
print("aAbByYzZaA".find("a"))
print("aAbByYzZaA".find("Z"))
print("aAbByYzZaA".find("D"))
print("aAbByYzZaA".find("a",1))
print("aAbByYzZaA".find("y",5))

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

# Demonstrando el método rfind():
txt = "Hello, welcome to my world."
print(txt.rfind("e"))
print(txt.rfind("e", 5, 10))


# Demonstrando el método index() y rindex():
print("aAbByYzZaA".index("a"))
print("aAbByYzZaA".rindex("a"))
print("aAbByYzZaA".index("D"))