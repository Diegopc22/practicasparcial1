"""Hacer un programa que lea 10 datos, si el dato es un numero se almacenara en un areglo 
si es un caracter o caracteres se metera a una lista, cuando fianlise el programa nos mostrara
cuantos elementos numeros y cuantos caracteres hay en cada estructura"""

d = 0
a = [0,0,0,0,0,0,0,0,0,0] #Arreglo
b = [] # lista
while(d <= 9):
     dato = input('Inegresa algun numero o letras: ')
     if dato.isdigit():
          a.append(dato)
          d += 1
     elif dato.isalpha():
          b.append(dato)
          d += 1
     else:
          print('No es valido')
print(f'Estos son tus numeros ingresados{a}')
print(f'Estas son las lerstras ingresadas{b}')
