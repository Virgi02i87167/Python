# Sets

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) # Inicialmente es un diccionario 'dict'

my_other_set = {'Jon','Alfa', 24}
print(type(my_other_set))

print(len(my_other_set))

my_other_set.add('Virgi02i87167')

print(my_other_set) # Un set no es una estructura ordenada

my_other_set.add('Virgi02i87167') # Un set no admite datos repetidos

print(my_other_set) 

print("Virgi02i87167" in my_other_set)
print("Virgi02i87" in my_other_set)

my_other_set.remove("Virgi02i87167")
print(my_other_set)

my_other_set.clear()
print(len(my_other_set))

del my_other_set
#print(my_other_set) NameError: name 'my_other_set' is not defined

my_set = {"Jon", "Alfa", 24}
my_list = list(my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Kotlin", "Swift", "Python"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"JavaScript", "C#"}))

print(my_new_set.difference(my_set))