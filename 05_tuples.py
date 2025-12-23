# Tuples

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (24, 1.70, 'Jona', "Hernandez", 'Jona')
my_other_tuple = (35, 60, 30)
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError

print(my_tuple.count('Jona'))
print(my_tuple.index('Hernandez'))
print(my_tuple.index('Jona'))

#my_tuple[1] = 1.80 no se pueden asignar nuevos item a las tuplas

my_sum_tumple = my_tuple + my_other_tuple
print(my_sum_tumple)

# Busca elementos entre el indice 2 y el 6
print(my_sum_tumple[2:6])

# Se cambia el tipado de tuple a list
my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[4] = 'Virgi02i87167'
my_tuple.insert(1, 'Azul')
my_tuple = tuple(my_tuple)
print(my_tuple)
print(tuple(my_tuple))

del my_tuple
#print(my_tuple) NameError: name 'my_tuple' is not defined