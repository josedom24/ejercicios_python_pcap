# Cifrado César.
texto = input("Ingresa tu mensaje: ")
cifrado = ''
for caracter in texto:
    if not caracter.isalpha():
        continue
    caracter = caracter.upper()
    code = ord(caracter) + 1
    if code > ord('Z'):
        code = ord('A')
    cifrado += chr(code)

print(cifrado)
