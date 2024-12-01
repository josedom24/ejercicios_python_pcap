from platform import platform

print(platform())        # Muestra la plataforma completa.
print(platform(True))       # Usa nombres alternativos para las capas.
print(platform(False, True))    # Usa nombres alternativos y muestra una forma más breve.
