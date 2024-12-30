class Uno:
    def opera(self):
        print("Escribo 1")

    def operacion(self):
        self.opera()

class Dos(Uno):
    def opera(self):
        print("Escribo 2")

objeto1 = Uno()
objeto2 = Dos()

objeto1.operacion()  # Salida: Escribo 1
objeto2.operacion()  # Salida: Escribo 2
