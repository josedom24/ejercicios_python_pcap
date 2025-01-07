def fun_con_return(n):
    for i in range(n):
        return i  # Se ejecuta solo una vez y termina el ciclo

def fun_con_yield(n):
    for i in range(n):
        yield i  # Pausa y reanuda la ejecución, recordando el estado

print(fun_con_return(10))
print(fun_con_yield(10))
for i in fun_con_yield(10):
	print(i)

