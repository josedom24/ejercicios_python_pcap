import time

class Estudiante:
    def tomar_descanso(self, seconds):
        print("Estoy muy cansado. Tengo que echarme una siesta. Hasta luego.")
        time.sleep(seconds)  # Suspende la ejecución durante el número de segundos especificado
        print("¡Dormí bien! ¡Me siento genial!")

# Creando una instancia de la clase Estudiante y llamando al método tomar_descanso
estudiante = Estudiante()
estudiante.tomar_descanso(5)  # La siesta dura 5 segundos
