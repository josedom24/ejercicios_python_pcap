class Stack:
    def __init__(self):
        self.__stack_list = []  # Lista privada para almacenar los elementos de la pila

    # Método para agregar un valor a la pila
    def push(self, val):
        self.__stack_list.append(val)

    # Método para quitar y devolver el valor en la parte superior de la pila
    def pop(self):
        val = self.__stack_list[-1]  # Obtiene el último elemento
        del self.__stack_list[-1]    # Elimina el último elemento
        return val

mipila = Stack()
mipila.push(3)
mipila.push(2)
mipila.push(1)

print(mipila.pop())
print(mipila.pop())
print(mipila.pop())