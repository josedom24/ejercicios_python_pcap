class PizzaError(Exception):
    def __init__(self, pizza, message):
        super().__init__(message)  # Llama al constructor de la clase base con el mensaje
        self.pizza = pizza  # Almacena información sobre la pizza

class TooMuchCheeseError(PizzaError):
    def __init__(self, pizza, cheese, message):
        super().__init__(pizza, message)  # Llama al constructor de PizzaError
        self.cheese = cheese  # Almacena información sobre el exceso de queso

# Ejemplo de uso
try:
    # Supongamos que una función chequea la cantidad de queso
    pizza_name = "Margarita"
    cheese_amount = 500  # en gramos
    if cheese_amount > 300:  # Suponiendo que 300g es el límite
        raise TooMuchCheeseError(pizza_name, cheese_amount, "Demasiado queso en la pizza.")
except TooMuchCheeseError as e:
    print("Error:", e," - Pizza:", e.pizza, "Queso: ", e.cheese, "g")
