class Stack:
    def __init__(self):
        self.__stack_list = []

stack_object = Stack()

# Intentar acceder a la lista desde fuera de la clase
print(len(stack_object.__stack_list))  # Esto dará error
