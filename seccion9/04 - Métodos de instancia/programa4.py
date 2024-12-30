class Clase:
    def otro_metodo(self):
        print("otro")  # Otro método dentro de la clase

    def metodo(self):
        print("método")
        self.otro_metodo()  # Invoca el método 'otro_metodo' usando self

obj = Clase()
obj.metodo()
