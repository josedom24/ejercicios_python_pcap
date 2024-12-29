class Stack:
    def __init__(self):
        self.__stack_list = []  # Lista privada para cada pila

    # Método para agregar un valor a la pila
    def push(self, val):
        self.__stack_list.append(val)

    # Método para quitar y devolver el último valor de la pila
    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


# Creación de dos objetos de la clase Stack
stack_object_1 = Stack()
stack_object_2 = Stack()

# Operaciones con ambas pilas
stack_object_1.push(3)  # Añade el valor 3 a la primera pila
stack_object_2.push(stack_object_1.pop())  # Pasa el valor de la primera pila a la segunda

# Muestra el valor de la segunda pila
print(stack_object_2.pop())  # Output: 3