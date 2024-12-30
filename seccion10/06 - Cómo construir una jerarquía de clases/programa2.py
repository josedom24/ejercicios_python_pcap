import time

class Vehiculo:
    def cambia_direccion(lado, on):
        pass

    def girar(self,lado):
        self.cambia_direccion(lado, True)
        time.sleep(0.25)
        self.cambia_direccion(lado, False)


class VehiculoOruga(Vehiculo):
    def control_giro(self, lado, stop):
        print("Pista:", lado, stop)

    def cambia_direccion(self, lado, on):
        self.control_giro(lado, on)


class VehiculoRueda(Vehiculo):
    def girar_ruedas_frontales(self, lado, on):
        print("Rueda:", lado, on)

    def cambia_direccion(self, lado, on):
        self.girar_ruedas_frontales(lado, on)

vehiculo1=VehiculoOruga()
vehiculo2=VehiculoRueda()
vehiculo1.girar("derecha")
vehiculo1.girar("izquierda")
vehiculo2.girar("derecha")
vehiculo2.girar("izquierda")

