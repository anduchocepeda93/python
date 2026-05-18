#tuplas
coordinates = (4,5)
print(coordinates[0])
print(coordinates[1]) 
#coordinates[0] = 10 #error, no se pueden modificar los elementos de una tupla
#sin embargo, se pueden modificar los elementos de una tupla si estos son mutables,
#por ejemplo, si la tupla contiene una lista, se puede modificar la lista
my_tuple = (1, 2, [3, 4, 5, 6], 7, [8, 9])
print(my_tuple)
my_tuple[4][1] = 10 
print(my_tuple)
