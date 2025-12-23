# Listas

my_list = list()
my_other_list = []

print(len(my_list))

my_list = [35, 24, 62, 52, 30, 30, 17]

print(my_list)
print(len(my_list))

my_other_list = [24, 1.70, 'Jona', "Hernandez"]

print(type(my_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[1])
print(my_other_list[-1])
print(my_other_list[-4])
print(my_list.count(24))
#print(my_other_list[4]) # IndexError
#print(my_other_list[-5]) # IndexError

# Decina variables a cada indice de la lista
age, height, name, surname = my_other_list
print(name, surname, age, height)

print(my_list + my_other_list)

# Agregar nuevo valor a la lista
my_other_list.append("Virgi02i87167")
print(my_other_list)

# Agregar nuevo valor en una posicion especifica
my_other_list.insert(1, "Rojo")
print(my_other_list)

# Cambia el valor que se encuentra en un indice especifica
my_other_list[1] = "Azul"
print(my_other_list)

# Elimina un valor
my_other_list.remove("Azul")
print(my_other_list)

my_list.remove(30)
print(my_list)

# Elimina el ultimo elemento
print(my_list.pop()) # nos mmuestra el pop que elimina
print(my_list)

print(my_list.pop(2))
print(my_list)

my_pop_element = my_list.pop(2)
print(my_pop_element)
print(my_list)

my_new_list =my_list.copy()

# Elimina por indice
del my_list[2]
print(my_list)


# Elimina toda la lista
my_list.clear()
print(my_list)
print(my_new_list)

# Imprime la lista al reverso
my_new_list.reverse()
print(my_new_list)

# Ordena de menor a mayor o de orden alfabetico
my_new_list.sort()
print(my_new_list)



# Esto no es una lista
my_list = 'Hola Python'
print(my_list)
print(type(my_list))