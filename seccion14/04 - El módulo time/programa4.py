import time

# Timestamp específico
timestamp = 1572879180

# Convertir a UTC
utc_time = time.gmtime(timestamp)
print(utc_time)

# Convertir a hora local
local_time = time.localtime(timestamp)
print(local_time)
