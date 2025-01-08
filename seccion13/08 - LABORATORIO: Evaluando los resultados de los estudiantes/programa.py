# Una clase de la excepción base para nuestro código:
class StudentsDataException(Exception):
    pass


# Una excepción para líneas erróneas:
class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_string):
        super().__init__(self)
        self.line_number = line_number
        self.line_string = line_string


# Una excepción para un archivo vacío.
class FileEmpty(StudentsDataException):
    def __init__(self):
        super().__init__(self)


from os import strerror

# Un diccionario para los datos de los estudiantes:
data = { }

file_name = input("Ingresa el nombre del archivo de datos del estudiante: ")
line_number = 1
try:
    f = open(file_name, "rt")
    # Leer el archivo completo en la lista.
    lines = f.readlines()
    f.close()
    # ¿El archivo está vacío?
    if len(lines) == 0:
        raise FileEmpty()
    # Escanee el archivo línea por línea.
    for i in range(len(lines)):
        # Obtener la línea n.
        line = lines[i]
        # Divídirlo en columnas.
        columns = line.split()
        # Debe haber 3 columnas, ¿están ahí?
        if len(columns) != 3:
            raise WrongLine(i + 1, line)
        # Construye una clave a partir del nombre y apellido del estudiante.
        student = columns[0] + ' ' + columns[1]
        # Obtener puntos.
        try:
            points = float(columns[2])
        except ValueError:
            raise WrongLine(i + 1, line)
        # Actualizar el diccionario.
        try:
            data[student] += points
        except KeyError:
            data[student] = points
    # Imprimir resultados.
    for student in sorted(data.keys()):
        print(student,'\t', data[student])

except IOError as e:
    print("Se produjo un error de E/S: ", strerror(e.errno))
except WrongLine as e:
    print("Línea incorrecta #" + str(e.line_number) + " en el archivo fuente:" + e.line_string)
except FileEmpty:
    print("Archivo fuente vacío")
    