# Hacer un programa que lea 10 numeros  # (ES) El programa debe leer 10 números | (EN) The program must read 10 numbers
# Y los alamcene en un arreglo          # (ES) Guardarlos en un arreglo (lista en Python) | (EN) Store them in an array (list in Python)

a = [0,0,0,0,0,0,0,0,0,0]  # (ES) Se crea una lista con 10 elementos inicializados en 0 | (EN) A list with 10 elements initialized at 0 is created

#Pafa formatear el dato pones un f antes de cadena y al final orchetes  
# (ES) Para usar f-strings se coloca una f antes de la cadena y llaves {} dentro | (EN) To use f-strings put an f before the string and braces {} inside

"""for i in range[0:10]:  
    a[i] = int(input(f'Escribe un numero'{i+1}))"""  # (ES) Ejemplo comentado con errores de sintaxis | (EN) Example commented with syntax errors

for i in range(0,10):  # (ES) Recorre los índices de 0 a 9 (10 posiciones) | (EN) Loops through indexes from 0 to 9 (10 positions)
    a[i] = int(input('Escribe un numero: \n'))  # (ES) Pide un número al usuario y lo guarda en la posición i | (EN) Asks the user for a number and stores it in position i

for i in a:  # (ES) Recorre cada número dentro de la lista a | (EN) Iterates through each number in list a
    print(i)  # (ES) Imprime cada número ingresado | (EN) Prints each entered number
