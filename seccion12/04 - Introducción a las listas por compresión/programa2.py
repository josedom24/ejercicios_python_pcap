the_list = [1 if x % 2 == 0 else 0 for x in range(10)]  # Lista por comprensión
the_generator = (1 if x % 2 == 0 else 0 for x in range(10))  # Generador

for v in the_list:
    print(v, end=" ")
print()

for v in the_generator:
    print(v, end=" ")
print()

print(the_list)
print(the_generator)

print(len(the_list))  # Devuelve 10
print(len(the_generator))  # Genera TypeError
