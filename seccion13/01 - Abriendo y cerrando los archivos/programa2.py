import errno

try:
    s = open("directorio/file.txt", "rt")
    # El procesamiento va aquí.
    s.close()
except Exception as exc:
    if exc.errno == errno.EACCES:
        print("Permiso denegado.")
    elif exc.errno == errno.EBADF:
        print("Número de archivo incorrecto.")
    elif exc.errno == errno.EEXIST:
        print("El archivo ya existe.")
    elif exc.errno == errno.EFBIG:
        print("El archivo es demasiado grande.")
    elif exc.errno == errno.EISDIR:
        print("Se ha tratado un directorio como archivo.")
    elif exc.errno == errno.EMFILE:
        print("Demasiados archivos abiertos.")
    elif exc.errno == errno.ENOENT:
        print("El archivo o directorio no existe.")
    elif exc.errno == errno.ENOSPC:
        print("No queda espacio en el dispositivo.")
    else:
        print("Error desconocido:", exc.errno)
