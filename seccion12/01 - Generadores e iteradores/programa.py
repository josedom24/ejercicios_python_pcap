class Fib:
    def __init__(self, nn):
        print("__init__")
        self.__n = nn  # Almacena el límite de la serie
        self.__i = 0   # Rastrea el índice actual
        self.__p1 = self.__p2 = 1  # Los dos números previos en la secuencia

    def __iter__(self):
        print("__iter__")
        return self  # Devuelve el propio objeto iterador

    def __next__(self):
        print("__next__")
        self.__i += 1  # Aumenta el índice
        if self.__i > self.__n:  # Si se excede el límite, se detiene
            raise StopIteration
        if self.__i in [1, 2]:  # Los primeros dos valores siempre son 1
            return 1
        ret = self.__p1 + self.__p2  # Calcula el siguiente número de Fibonacci
        self.__p1, self.__p2 = self.__p2, ret  # Actualiza los valores previos
        return ret

# Uso del iterador:
for i in Fib(10):
    print(i)
