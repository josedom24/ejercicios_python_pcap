import time

timestamp = 1572879180  # Ejemplo de marca de tiempo
st = time.gmtime(timestamp)

# Formatear usando un objeto struct_time
print(time.strftime("%Y/%m/%d %H:%M:%S", st))

# Formatear la hora local actual
print(time.strftime("%Y/%m/%d %H:%M:%S"))
