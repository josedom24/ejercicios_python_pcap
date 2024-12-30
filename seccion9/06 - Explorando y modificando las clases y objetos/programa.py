class Clase:
    pass
objeto = Clase()
objeto.a = 1
objeto.b = 2
objeto.i = 3
objeto.num_real = 3.5
objeto.num_entero = 4
objeto.z = 5

def incIntsI(objeto):
    for name in objeto.__dict__.keys():
        if name.startswith('i'):
            val = getattr(objeto, name)
            if isinstance(val, int):
                setattr(objeto, name, val + 1)

print(objeto.__dict__)
incIntsI(objeto)
print(objeto.__dict__)
