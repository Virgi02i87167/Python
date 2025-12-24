# Loops

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:  # Es opcional
    print("Mi condicion es mayor o igual que 10")

print("La ejecucion continua")

while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print("Se detiene la ejecucion")
        break
    print("Mi condicion es menor que 20")

print("La ejecucion continua")

# For

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)

my_tuple = (24, 1.70, "Jona", "Alfa", "Jona")
for element in my_tuple:
    print(element)

my_set = {"Jona", "Alfa", 24}
for element in my_set:
    print(element)

my_dict = {"Nombre": "Jon", "Apellido": "Alfa", "Edad": 24, 1: "Python"}

for element in my_dict:
    print(element)
    if element == "Edad":
        break
else:
    print("El bucle for para el diccionario ha finalizado")

print("La ejecución continúa")

for element in my_dict:
    print(element)
    if element == "Edad":
        continue
    print("Se ejecuta")
else:
    print("El bluce for para diccionario ha finalizado")