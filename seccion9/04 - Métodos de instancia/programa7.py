class Clase:
    def visible(self):
        print("visible")
    
    def __oculto(self):
        print("oculto")


obj = Clase()
obj.visible()

try:
    obj.__oculto()
except:
    print("fallido")

obj._Clase__oculto()
