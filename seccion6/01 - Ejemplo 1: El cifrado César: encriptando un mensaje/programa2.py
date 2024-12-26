# Cifrado César - descifrar un mensaje.
cifrado = input('Ingresa tu criptograma: ')
texto = ''
for caracter in cifrado:
    if not caracter.isalpha():
        continue
    caracter = caracter.upper()
    code = ord(caracter) - 1
    if code < ord('A'):
        code = ord('Z')
    texto += chr(code)

print(texto)
