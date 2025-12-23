# Variables
mi_variable = "My String variable"
print(mi_variable)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable = str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenacion de variables en un print
print(mi_variable, my_int_to_str_variable, my_bool_variable)
print("Este es el valor de:", my_bool_variable)

# Funciones del sistema
print(len(mi_variable))

# Variables en una sola linea
name, surname, alias, age = "Jona", "Alfaro", "Virgi02i87167", 24
print("Me llamo:", name, surname, "Mi edad es", age, "Y mi alias es:", alias)

# Inputs
"""
name = input('¿Cual es tu nombre? ')
age = input('¿Cual es tu edad? ')
print(name)
print(age)
"""

# Cambiamos el tipo
name = 24
age = "Jon"
print(name)
print(age)

# ¿Forzamos el tipo?
address: str = "Mi direccion"
address: int = 32
print(type(address))