class PizzaError(Exception):
    def __init__(self, pizza='desconocida', message=''):
        super().__init__(message)  # Llama al constructor de la clase base
        self.pizza = pizza  # Almacena información sobre la pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza='desconocida', cheese='>100', message=''):
        super().__init__(pizza, message)  # Llama al constructor de PizzaError
        self.cheese = cheese  # Almacena información sobre el exceso de queso

def make_pizza(pizza, cheese):
    if pizza not in ['margherita', 'capricciosa', 'calzone']:
        raise PizzaError(pizza, "no hay tal pizza en el menú")  # Lanza PizzaError si la pizza no está en el menú
    if cheese > 100:
        raise TooMuchCheeseError(pizza, cheese, "demasiado queso")  # Lanza TooMuchCheeseError si hay demasiado queso
    print("¡Pizza lista!")  # Indica que la pizza se ha preparado correctamente

# Prueba de la función con diferentes entradas
for (pz, ch) in [('calzone', 0), ('margherita', 110), ('mafia', 20)]:
    try:
        make_pizza(pz, ch)  # Intenta hacer la pizza
    except TooMuchCheeseError as tmce:
        print(tmce, ':', tmce.cheese)  # Maneja el error de exceso de queso
    except PizzaError as pe:
        print(pe, ':', pe.pizza)  # Maneja el error de pizza no válida
