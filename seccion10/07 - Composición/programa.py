import time

class Orugas:
    def cambiar_direccion(self, lado, on):
        print("pistas: ", lado, on)

class Ruedas:
    def cambiar_direccion(self, lado, on):
        print("ruedas: ", lado, on)

class Vehiculo:
    def __init__(self, controlador):
        self.controlador = controlador

    def girar(self, lado):
        self.controlador.cambiar_direccion(lado, True)
        time.sleep(0.25)
        self.controlador.cambiar_direccion(lado, False)

# Creamos vehículos con diferentes controladores
vehiculooruga = Vehiculo(Ruedas())
vehiculorueda = Vehiculo(Orugas())

vehiculooruga.girar("Izquierda")  # El vehículo con ruedas gira a la izquierda
vehiculorueda.girar("Derecha")  # El vehículo con orugas gira a la derecha
