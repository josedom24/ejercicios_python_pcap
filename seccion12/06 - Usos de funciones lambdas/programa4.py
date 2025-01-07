from random import seed, randint

def es_par_y_positivo(x):
    return x > 0 and x % 2 == 0

seed()
data = [randint(-10,10) for x in range(5)]
filtered = list(filter(es_par_y_positivo, data))

print(data)
print(filtered)
