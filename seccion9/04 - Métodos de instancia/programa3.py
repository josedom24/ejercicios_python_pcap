class Clase:
    varia = 2  # Variable de clase

    def metodo(self):
        print(self.varia, self.var)  # Acceso a variable de clase e instancia

obj = Clase()
obj.var = 3  # Variable de instancia asignada a este objeto
obj.metodo()  # Invocamos el método que accede a ambas variables
