"""Hacer un programa que lea 10 datos, si el dato es un numero se almacenara en un arreglo 
si es un caracter o caracteres se meterá a una lista, cuando finalice el programa nos mostrará
cuantos elementos números y cuantos caracteres hay en cada estructura"""  
# (ES) Explicación del programa | (EN) Program description

d = 0  # (ES) Contador de datos ingresados | (EN) Counter of entered data
a = [0,0,0,0,0,0,0,0,0,0]  # (ES) Arreglo inicializado con 10 ceros | (EN) Array initialized with 10 zeros
b = []  # (ES) Lista vacía para guardar letras | (EN) Empty list to store letters

while(d <= 9):  # (ES) Bucle hasta que se ingresen 10 datos válidos | (EN) Loop until 10 valid inputs are entered
     dato = input('Ingresa algun numero o letras: ')  # (ES) Solicita al usuario un dato | (EN) Asks the user for a value
     if dato.isdigit():  # (ES) Si el dato son solo dígitos | (EN) If the input is only digits
          a.append(dato)  # (ES) Agrega el número a la lista 'a' | (EN) Appends the number to 'a'
          d += 1  # (ES) Incrementa el contador de datos válidos | (EN) Increments valid data counter
     elif dato.isalpha():  # (ES) Si el dato son solo letras | (EN) If the input is only letters
          b.append(dato)  # (ES) Agrega la letra a la lista 'b' | (EN) Appends the letter to 'b'
          d += 1  # (ES) Incrementa el contador de datos válidos | (EN) Increments valid data counter
     else:
          print('No es valido')  # (ES) Mensaje si el dato no es número ni letra | (EN) Message if input is not number or letter

print(f'Estos son tus numeros ingresados {a}')  # (ES) Muestra los números | (EN) Shows the numbers
print(f'Estas son las letras ingresadas{b}')