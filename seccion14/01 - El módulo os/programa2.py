import os

## Creación de directorios

os.mkdir("directorio1")
print(os.listdir())

## Creación recursiva de directorios

os.makedirs("directorio2/directorio3")
os.chdir("directorio2")
print(os.listdir())

# Averiguar el directorio donde estamos

print(os.getcwd())
os.chdir("directorio3")
print(os.getcwd())

# Eliminar directorios

os.chdir("..")
os.chdir("..")
print(os.listdir())  
os.rmdir("directorio1")  
print(os.listdir())  

os.removedirs("directorio2/directorio3") 
print(os.listdir())  

