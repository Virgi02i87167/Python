# Functions

# Definición
def my_function ():
    print("Esto es una funcion")

my_function()
my_function()

# Función con parámetros de entrada/argumentos
def sum_two_values(first_value: int, second_value):
    print(first_value + second_value)

sum_two_values(5, 7)
sum_two_values(54754, 71231)
sum_two_values("5", "7")
sum_two_values(1.4, 5.2)

# Función con parámetros de entrada/argumentos y retorno
def sum_two_values_with_return(first_value, second_value):
    my_sum = first_value + second_value
    return my_sum

my_result = sum_two_values(1.4, 5.2)
print(my_result)

my_result = sum_two_values_with_return(10, 5)
print(my_result)

# Función con parámetros de entrada/argumentos por clave
def print_name(name, surname):
    print(f"{name} {surname}")

print_name(surname="Jona", name="Virgi")

# Función con parámetros de entrada/argumentos por defecto
def print_name_with_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_with_default("Jona", "Alfa")
print_name_with_default("Jona", "Alfa" ,"Virgi02i87167")

# Función con parámetros de entrada/argumentos arbitrarios
def print_texts(*texts):
    print(type(texts))
    for text in texts:
        print(text.upper())

print_texts("Hola", "Python",  "Virgi02i87167")
print_texts("Hola")