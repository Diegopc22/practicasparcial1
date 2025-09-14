a = [10]  # (ES) Se crea una lista con un solo elemento: 10 | (EN) A list is created with a single element: 10
b = []  # (ES) Se crea una lista vacía | (EN) An empty list is created
b.append(10000)  # (ES) Se agrega el número 10000 a la lista b | (EN) Adds the number 10000 to list b
b = {'hola', 10, 10.05, False, 'm'}  # (ES) Se reemplaza b con un conjunto (set) que contiene varios elementos | (EN) b is replaced with a set containing several elements

print(a[0])  # (ES) Imprimwe el primer elemento de la lista a, que es 10 | (EN) Prints the first element of list a, which is 10

if len(a) > len(b):  # (ES) Compara el tamaño de la lista a con el del conjunto b | (EN) Compares the size of list a with that of set b
    print('A es mayor')  # (ES) Se imprime si la lista a tiene más elementos | (EN) Prints if list a has more elements
else:  
    print('B es mayor')  # (ES) Se imprime si el conjunto b tiene más o igual cantidad de elementos | (EN) Prints if set b has more or the same number of elements

for i in a:  # (ES) Recorre cada elemento de la lista a | (EN) Iterates over each element in list a
    print(a)  # (ES) Imprime toda la lista a en cada iteración (a = [10]) | (EN) Prints the entire list a in each iteration (a = [10])
