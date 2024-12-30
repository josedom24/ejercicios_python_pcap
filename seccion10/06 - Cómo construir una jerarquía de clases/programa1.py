import time

class VehiculoOruga:
    def control_giro(self, lado, stop):
        print("Pista:", lado, stop)

    def girar(self, lado):
        self.control_giro(lado, True)
        time.sleep(0.25)
        self.control_giro(lado, False)

class VehiculoRueda:
    def girar_ruedas_frontales(self, lado, on):
        print("Rueda:", lado, on)

    def girar(self, lado):
        self.girar_ruedas_frontales(lado, True)
        time.sleep(0.25)
        self.girar_ruedas_frontales(lado, False)

vehiculo1=VehiculoOruga()
vehiculo2=VehiculoRueda()
vehiculo1.girar("derecha")
vehiculo1.girar("izquierda")
vehiculo2.girar("derecha")
vehiculo2.girar("izquierda")

